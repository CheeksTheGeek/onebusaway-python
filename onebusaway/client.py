# client.py
import requests
import requests.packages
from datetime import datetime
import os
from typing import Any, Dict, List, Optional
from .models import (
    Response,
    Agency,
    ArrivalAndDeparture,
    StopWithArrivalsAndDepartures,
    Block,
    Route,
    RouteSchedule,
    EncodedPolyline,
    Stop,
    StopsForRoute,
    TripDetails,
    Trip,
    VehicleStatus,
    StopSchedule,
    AgencyDetails,
    DateTime,
)
from .utils import dynamic_dataclass_from_dict

from .exceptions import (
    OneBusAwayException,
    APIKeyMissingError,
    APIKeyInvalidError,
    BadRequestError,
    NotFoundError,
    ServerError,
    ResponseParseError,
    DataValidationError,
    StopNotFoundError,
    TripNotFoundError,
)


class OneBusAway:
    def __init__(
        self,
        base_url: str = "api.pugetsound.onebusaway.org",
    ):
        self.api_key = os.environ.get("OBA_API_KEY") or "TEST"

        self.base_url = base_url
        self.base_path = "/api/where"
        # Create a session to persist the API key
        self.session = requests.Session()
        self.session.params = {"key": self.api_key}

        # Disable SSL warnings
        requests.packages.urllib3.disable_warnings(
            requests.packages.urllib3.exceptions.InsecureRequestWarning
        )

    def _get_json_dict(
        self, path: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        # add API key to params
        if params is None:
            params = {}
        # throw an error if the API key is added to the params via the method
        if "key" in params:
            raise ValueError("API key should not be added to the params")
        params["key"] = self.api_key
        response = self.session.get(
            f"https://{self.base_url}{self.base_path}{path}", params=params
        )
        response.raise_for_status()
        return response.json()

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Response:
        json_dict = self._get_json_dict(path, params)
        return Response(**json_dict) if json_dict else Response()

    def agency_with_coverage(self, get_references: bool = False) -> List[Agency]:
        response = self._get("/agencies-with-coverage.json")
        if isinstance(response.data, dict):
            return (
                [
                    Agency(
                        **agency,
                        linked_references=True,
                        references=response.data.get("references", {}),
                    )
                    for agency in response.data.get("list", [])
                ]
                if get_references
                else [Agency(**agency) for agency in response.data.get("list", [])]
            )
        elif isinstance(response.data, list):
            return [Agency(**agency) for agency in response.data]
        else:
            raise ValueError("Unexpected response data type")

    def agency(self, id: str, get_references: bool = False) -> Agency:
        response = self._get(f"/agency/{id}.json")
        return (
            AgencyDetails(
                **response.data["entry"],
                linked_references=True,
                references=response.data.get("references", {}),
            )
            if get_references
            else AgencyDetails(**response.data["entry"])
        )

    def arrival_and_departure_for_stop(
        self,
        id: str,
        tripId: str,
        serviceDate: int,
        vehicleId: Optional[str] = None,
        stopSequence: Optional[int] = None,
        get_references: bool = False,
    ) -> ArrivalAndDeparture:
        params = {
            "tripId": tripId,
            "serviceDate": serviceDate,
        }
        if vehicleId is not None:
            params["vehicleId"] = vehicleId
        if stopSequence is not None:
            params["stopSequence"] = stopSequence
        response = self._get(f"/arrival-and-departure-for-stop/{id}.json", params)
        return (
            ArrivalAndDeparture(
                **response.data["entry"],
                linked_references=True,
                references=response.data.get("references", {}),
            )
            if get_references
            else ArrivalAndDeparture(**response.data["entry"])
        )

    def arrivals_and_departures_for_stop(
        self,
        id: str,
        minutesBefore: Optional[int] = None,
        minutesAfter: Optional[int] = None,
        get_references: bool = False,
    ) -> StopWithArrivalsAndDepartures:
        params = {}
        if minutesBefore is not None:
            params["minutesBefore"] = minutesBefore
        if minutesAfter is not None:
            params["minutesAfter"] = minutesAfter
        response = self._get(f"/arrivals-and-departures-for-stop/{id}.json", params)
        return (
            StopWithArrivalsAndDepartures(
                **response.data["entry"],
                linked_references=True,
                references=response.data.get("references", {}),
            )
            if get_references
            else StopWithArrivalsAndDepartures(**response.data["entry"])
        )

    def block(self, id: str, get_references: bool = False) -> Block:
        response = self._get(f"/block/{id}.json")
        return (
            Block(
                **response.data["entry"],
                linked_references=True,
                references=response.data.get("references", {}),
            )
            if get_references
            else Block(**response.data["entry"])
        )

    def get_config(self, get_references: bool = False) -> Dict[str, Any]:
        response = self._get("/config.json")
        return dynamic_dataclass_from_dict(response.data["entry"], "OBASetupConfig")

    def current_time(self, get_references: bool = False) -> datetime:
        response = self._get("/current-time.json")
        return (
            DateTime(
                **response.data["entry"],
                linked_references=True,
                references=response.data.get("references", {}),
            )
            if get_references
            else DateTime(**response.data["entry"])
        )

    def report_problem_with_stop(
        self,
        stopId: str,
        code: str,
        userComment: Optional[str] = None,
        userLat: Optional[float] = None,
        userLon: Optional[float] = None,
        userLocationAccuracy: Optional[float] = None,
    ) -> bool:
        params = {
            "code": code,
        }
        if userComment is not None:
            params["userComment"] = userComment
        if userLat is not None:
            params["userLat"] = userLat
        if userLon is not None:
            params["userLon"] = userLon
        if userLocationAccuracy is not None:
            params["userLocationAccuracy"] = userLocationAccuracy
        return (
            True
            if self._get(f"/report-problem-with-stop/{stopId}.json", params).text
            == "OK"
            else False
        )

    def report_problem_with_trip(
        self,
        tripId: str,
        serviceDate: int,
        vehicleId: str,
        stopId: str,
        code: str,
        userComment: Optional[str] = None,
        userOnVehicle: Optional[bool] = None,
        userVehicleNumber: Optional[str] = None,
        userLat: Optional[float] = None,
        userLon: Optional[float] = None,
        userLocationAccuracy: Optional[float] = None,
    ) -> None:
        params = {
            "serviceDate": serviceDate,
            "vehicleId": vehicleId,
            "stopId": stopId,
            "code": code,
        }
        if userComment is not None:
            params["userComment"] = userComment
        if userOnVehicle is not None:
            params["userOnVehicle"] = userOnVehicle
        if userVehicleNumber is not None:
            params["userVehicleNumber"] = userVehicleNumber
        if userLat is not None:
            params["userLat"] = userLat
        if userLon is not None:
            params["userLon"] = userLon
        if userLocationAccuracy is not None:
            params["userLocationAccuracy"] = userLocationAccuracy
        return (
            True
            if self._get(f"/report-problem-with-trip/{tripId}.json", params).text
            == "OK"
            else False
        )

    def route_ids_for_agency(self, id: str, get_references: bool = False) -> List[str]:
        response = self._get(f"/route-ids-for-agency/{id}.json")
        return response.data["list"]

    def route(self, id: str, get_references: bool = False) -> Route:
        response = self._get(f"/route/{id}.json")
        return Route(**response.data["entry"])

    def routes_for_agency(self, id: str, get_references: bool = False) -> List[Route]:
        response = self._get(f"/routes-for-agency/{id}.json")
        return [Route(**route) for route in response.data["list"]]

    def routes_for_location(
        self,
        lat: float,
        lon: float,
        radius: Optional[int] = None,
        latSpan: Optional[float] = None,
        lonSpan: Optional[float] = None,
        query: Optional[str] = None,
        get_references: bool = False,
    ) -> List[Route]:
        params = {
            "lat": lat,
            "lon": lon,
        }
        if radius is not None:
            params["radius"] = radius
        if latSpan is not None:
            params["latSpan"] = latSpan
        if lonSpan is not None:
            params["lonSpan"] = lonSpan
        if query is not None:
            params["query"] = query
        response = self._get("/routes-for-location.json", params)
        return [Route(**route) for route in response.data["list"]]

    def schedule_for_route(
        self, id: str, date: Optional[str] = None, get_references: bool = False
    ) -> RouteSchedule:
        params = {}
        if date is not None:
            params["date"] = date
        response = self._get(f"/schedule-for-route/{id}.json", params)
        return RouteSchedule(**response.data["entry"])

    def schedule_for_stop(
        self, id: str, date: Optional[str] = None, get_references: bool = False
    ) -> StopSchedule:
        params = {}
        if date is not None:
            params["date"] = date
        response = self._get(f"/schedule-for-stop/{id}.json", params)
        return StopSchedule(**response.data["entry"])

    def shape(self, id: str, get_references: bool = False) -> EncodedPolyline:
        response = self._get(f"/shape/{id}.json")
        return EncodedPolyline(**response.data["entry"])

    def stop_ids_for_agency(self, id: str, get_references: bool = False) -> List[str]:
        response = self._get(f"/stop-ids-for-agency/{id}.json")
        return response.data["list"]

    def stop(self, id: str, get_references: bool = False) -> Stop:
        response = self._get(f"/stop/{id}.json")
        # return Stop(**response.data["entry"]) if response.data
        if response.code == 200:
            return Stop(**response.data["entry"])
        else:
            raise NotFoundError(response.text)

    def stops_for_location(
        self,
        lat: float,
        lon: float,
        radius: Optional[int] = None,
        latSpan: Optional[float] = None,
        lonSpan: Optional[float] = None,
        query: Optional[str] = None,
        get_references: bool = False,
    ) -> List[Stop]:
        params = {
            "lat": lat,
            "lon": lon,
        }
        if radius is not None:
            params["radius"] = radius
        if latSpan is not None:
            params["latSpan"] = latSpan
        if lonSpan is not None:
            params["lonSpan"] = lonSpan
        if query is not None:
            params["query"] = query
        response = self._get("/stops-for-location.json", params)
        return [Stop(**stop) for stop in response.data["list"]]

    def stops_for_route(
        self,
        id: str,
        includePolylines: Optional[bool] = None,
        time: Optional[str] = None,
        get_references: bool = False,
    ) -> StopsForRoute:
        params = {}
        if includePolylines is not None:
            params["includePolylines"] = includePolylines
        if time is not None:
            params["time"] = time
        response = self._get(f"/stops-for-route/{id}.json", params)
        return StopsForRoute(**response.data["entry"])

    def trip_details(
        self,
        id: str,
        serviceDate: Optional[int] = None,
        includeTrip: Optional[bool] = None,
        includeSchedule: Optional[bool] = None,
        includeStatus: Optional[bool] = None,
        time: Optional[str] = None,
        get_references: bool = False,
    ) -> TripDetails:
        params = {}
        if serviceDate is not None:
            params["serviceDate"] = serviceDate
        if includeTrip is not None:
            params["includeTrip"] = includeTrip
        if includeSchedule is not None:
            params["includeSchedule"] = includeSchedule
        if includeStatus is not None:
            params["includeStatus"] = includeStatus
        if time is not None:
            params["time"] = time
        response = self._get(f"/trip-details/{id}.json", params)
        return TripDetails(**response.data["entry"])

    def trip_for_vehicle(
        self,
        id: str,
        includeTrip: Optional[bool] = None,
        includeSchedule: Optional[bool] = None,
        includeStatus: Optional[bool] = None,
        time: Optional[str] = None,
        get_references: bool = False,
    ) -> TripDetails:
        params = {}
        if includeTrip is not None:
            params["includeTrip"] = includeTrip
        if includeSchedule is not None:
            params["includeSchedule"] = includeSchedule
        if includeStatus is not None:
            params["includeStatus"] = includeStatus
        if time is not None:
            params["time"] = time
        response = self._get(f"/trip-for-vehicle/{id}.json", params)
        return TripDetails(**response.data["entry"])

    def trip(self, id: str, get_references: bool = False) -> Trip:
        response = self._get(f"/trip/{id}.json")
        return Trip(**response.data["entry"])

    def trips_for_location(
        self,
        lat: float,
        lon: float,
        latSpan: float,
        lonSpan: float,
        includeTrip: Optional[bool] = None,
        includeSchedule: Optional[bool] = None,
        time: Optional[str] = None,
        get_references: bool = False,
    ) -> List[TripDetails]:
        params = {
            "lat": lat,
            "lon": lon,
            "latSpan": latSpan,
            "lonSpan": lonSpan,
        }
        if includeTrip is not None:
            params["includeTrip"] = includeTrip
        if includeSchedule is not None:
            params["includeSchedule"] = includeSchedule
        if time is not None:
            params["time"] = time
        response = self._get("/trips-for-location.json", params)
        return [TripDetails(**trip) for trip in response.data["list"]]

    def trips_for_route(
        self,
        id: str,
        includeStatus: Optional[bool] = None,
        includeSchedule: Optional[bool] = None,
        time: Optional[str] = None,
        get_references: bool = False,
    ) -> List[TripDetails]:
        params = {}
        if includeStatus is not None:
            params["includeStatus"] = includeStatus
        if includeSchedule is not None:
            params["includeSchedule"] = includeSchedule
        if time is not None:
            params["time"] = time
        response = self._get(f"/trips-for-route/{id}.json", params)
        return [TripDetails(**trip) for trip in response.data["list"]]

    def vehicles_for_agency(
        self, id: str, time: Optional[str] = None, get_references: bool = False
    ) -> List[VehicleStatus]:
        params = {}
        if time is not None:
            params["time"] = time
        response = self._get(f"/vehicles-for-agency/{id}.json", params)
        return [VehicleStatus(**vehicle) for vehicle in response.data["list"]]
