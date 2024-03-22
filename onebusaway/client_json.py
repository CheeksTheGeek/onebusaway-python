import requests
import requests.packages
from typing import Any, Dict, Optional
import os


# BAREMETAL CLIET, HELPS GENERATE SCHEMAS
class OneBusAwayJSON:
    def __init__(
        self,
        base_url: str = "api.pugetsound.onebusaway.org",
    ):
        self.api_key = os.environ.get("ONEBUSAWAY_API_KEY") or "TEST"
        self.base_url = base_url
        self.base_path = "/api/where"
        # Create a session to persist the API key
        self.session = requests.Session()
        self.session.params = {"key": self.api_key}

        # Disable SSL warnings
        requests.packages.urllib3.disable_warnings(
            requests.packages.urllib3.exceptions.InsecureRequestWarning
        )

    def _get_json_dict(self, path: str, params: Optional[Dict[str, Any]] = None):
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
        return response

    def agency_with_coverage(self):
        return self._get_json_dict("/agencies-with-coverage.json")

    def agency(self, id: str):
        return self._get_json_dict(f"/agency/{id}.json")

    def arrival_and_departure_for_stop(
        self,
        id: str,
        tripId: str,
        serviceDate: int,
        vehicleId: Optional[str] = None,
        stopSequence: Optional[int] = None,
    ):
        params = {
            "tripId": tripId,
            "serviceDate": serviceDate,
        }
        if vehicleId is not None:
            params["vehicleId"] = vehicleId
        if stopSequence is not None:
            params["stopSequence"] = stopSequence
        return self._get_json_dict(f"/arrival-and-departure-for-stop/{id}.json", params)

    def arrivals_and_departures_for_stop(
        self,
        id: str,
        minutesBefore: Optional[int] = None,
        minutesAfter: Optional[int] = None,
    ):
        params = {}
        if minutesBefore is not None:
            params["minutesBefore"] = minutesBefore
        if minutesAfter is not None:
            params["minutesAfter"] = minutesAfter
        return self._get_json_dict(
            f"/arrivals-and-departures-for-stop/{id}.json", params
        )

    def block(self, id: str):
        return self._get_json_dict(f"/block/{id}.json")

    def get_config(self):
        return self._get_json_dict("/config.json")

    def current_time_unix_epoch(self):
        return self._get_json_dict("/current-time.json")

    def current_time(self):
        return self._get_json_dict("/current-time.json")

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
        return self._get_json_dict(f"/report-problem-with-stop/{stopId}.json", params)

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
    ):
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
        return self._get_json_dict(f"/report-problem-with-trip/{tripId}.json", params)

    def route_ids_for_agency(self, id: str):
        return self._get_json_dict(f"/route-ids-for-agency/{id}.json")

    def route(self, id: str):
        return self._get_json_dict(f"/route/{id}.json")

    def routes_for_agency(self, id: str):
        return self._get_json_dict(f"/routes-for-agency/{id}.json")

    def routes_for_location(
        self,
        lat: float,
        lon: float,
        radius: Optional[int] = None,
        latSpan: Optional[float] = None,
        lonSpan: Optional[float] = None,
        query: Optional[str] = None,
    ):
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
        return self._get_json_dict("/routes-for-location.json", params)

    def schedule_for_route(self, id: str, date: Optional[str] = None):
        params = {}
        if date is not None:
            params["date"] = date
        return self._get_json_dict(f"/schedule-for-route/{id}.json", params)

    def schedule_for_stop(self, id: str, date: Optional[str] = None):
        params = {}
        if date is not None:
            params["date"] = date
        return self._get_json_dict(f"/schedule-for-stop/{id}.json", params)

    def shape(self, id: str):
        return self._get_json_dict(f"/shape/{id}.json")

    def stop_ids_for_agency(self, id: str):
        return self._get_json_dict(f"/stop-ids-for-agency/{id}.json")

    def stop(self, id: str):
        return self._get_json_dict(f"/stop/{id}.json")

    def stops_for_location(
        self,
        lat: float,
        lon: float,
        radius: Optional[int] = None,
        latSpan: Optional[float] = None,
        lonSpan: Optional[float] = None,
        query: Optional[str] = None,
    ):
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
        return self._get_json_dict("/stops-for-location.json", params)

    def stops_for_route(
        self,
        id: str,
        includePolylines: Optional[bool] = None,
        time: Optional[str] = None,
    ):
        params = {}
        if includePolylines is not None:
            params["includePolylines"] = includePolylines
        if time is not None:
            params["time"] = time
        return self._get_json_dict(f"/stops-for-route/{id}.json", params)

    def trip_details(
        self,
        id: str,
        serviceDate: Optional[int] = None,
        includeTrip: Optional[bool] = None,
        includeSchedule: Optional[bool] = None,
        includeStatus: Optional[bool] = None,
        time: Optional[str] = None,
    ):
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
        return self._get_json_dict(f"/trip-details/{id}.json", params)

    def trip_for_vehicle(
        self,
        id: str,
        includeTrip: Optional[bool] = None,
        includeSchedule: Optional[bool] = None,
        includeStatus: Optional[bool] = None,
        time: Optional[str] = None,
    ):
        params = {}
        if includeTrip is not None:
            params["includeTrip"] = includeTrip
        if includeSchedule is not None:
            params["includeSchedule"] = includeSchedule
        if includeStatus is not None:
            params["includeStatus"] = includeStatus
        if time is not None:
            params["time"] = time
        return self._get_json_dict(f"/trip-for-vehicle/{id}.json", params)

    def trip(self, id: str):
        return self._get_json_dict(f"/trip/{id}.json")

    def trips_for_location(
        self,
        lat: float,
        lon: float,
        latSpan: float,
        lonSpan: float,
        includeTrip: Optional[bool] = None,
        includeSchedule: Optional[bool] = None,
        time: Optional[str] = None,
    ):
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
        return self._get_json_dict("/trips-for-location.json", params)

    def trips_for_route(
        self,
        id: str,
        includeStatus: Optional[bool] = None,
        includeSchedule: Optional[bool] = None,
        time: Optional[str] = None,
    ):
        params = {}
        if includeStatus is not None:
            params["includeStatus"] = includeStatus
        if includeSchedule is not None:
            params["includeSchedule"] = includeSchedule
        if time is not None:
            params["time"] = time
        return self._get_json_dict(f"/trips-for-route/{id}.json", params)

    def vehicles_for_agency(
        self,
        id: str,
        time: Optional[str] = None,
    ):
        params = {}
        if time is not None:
            params["time"] = time
        return self._get_json_dict(f"/vehicles-for-agency/{id}.json", params)
