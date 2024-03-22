# test_client.py
import pytest
from unittest.mock import patch, Mock
from onebusaway import OneBusAway, NotFoundError, ServerError


@pytest.fixture
def client():
    return OneBusAway()


class TestOneBusAway:
    @patch("onebusaway.client.requests.Session.get")
    def test_agency_with_coverage(self, mock_get, client):
        mock_response = Mock()
        mock_response.json.return_value = {
            "data": {
                "list": [
                    {
                        "agencyId": "agency1",
                        "lat": 47.6,
                        "lon": -122.3,
                        "latSpan": 0.1,
                        "lonSpan": 0.1,
                    }
                ]
            }
        }
        mock_get.return_value = mock_response
        agencies = client.agency_with_coverage()
        assert len(agencies) == 1
        agency = agencies[0]
        assert agency.agencyId == "agency1"
        assert agency.lat == 47.6
        assert agency.lon == -122.3
        assert agency.latSpan == 0.1
        assert agency.lonSpan == 0.1

        @patch("onebusaway.client.requests.Session.get")
        def test_agency(self, mock_get, client):
            mock_response = Mock()
            mock_response.json.return_value = {
                "data": {
                    "entry": {
                        "agencyId": "agency1",
                        "name": "Agency 1",
                        "url": "http://agency1.com",
                    }
                }
            }
            mock_get.return_value = mock_response
            agency = client.agency("agency1")
            assert agency.agencyId == "agency1"
            assert agency.name == "Agency 1"
            assert agency.url == "http://agency1.com"

    # def arrival_and_departure_for_stop(
    #     self,
    #     id: str,
    #     tripId: str,
    #     serviceDate: int,
    #     vehicleId: Optional[str] = None,
    #     stopSequence: Optional[int] = None,
    #     get_references: bool = False,
    # ) -> ArrivalAndDeparture:
    #     params = {
    #         "tripId": tripId,
    #         "serviceDate": serviceDate,
    #     }
    #     if vehicleId is not None:
    #         params["vehicleId"] = vehicleId
    #     if stopSequence is not None:
    #         params["stopSequence"] = stopSequence
    #     response = self._get(f"/arrival-and-departure-for-stop/{id}.json", params)
    #     return (
    #         ArrivalAndDeparture(
    #             **response.data["entry"],
    #             linked_references=True,
    #             references=response.data.get("references", {}),
    #         )
    #         if get_references
    #         else ArrivalAndDeparture(**response.data["entry"])
    #     )
    # @dataclass
    # class ArrivalAndDeparture:
    #     actualTrack: str
    #     arrivalEnabled: bool
    #     blockTripSequence: int
    #     departureEnabled: bool
    #     distanceFromStop: float
    #     frequency: str
    #     historicalOccupancy: str
    #     lastUpdateTime: int
    #     numberOfStopsAway: int
    #     occupancyStatus: str
    #     predicted: bool
    #     predictedArrivalInterval: str
    #     predictedArrivalTime: int
    #     predictedDepartureInterval: str
    #     predictedDepartureTime: int
    #     predictedOccupancy: str
    #     routeId: str
    #     routeLongName: str
    #     routeShortName: str
    #     scheduledArrivalInterval: str
    #     scheduledArrivalTime: int
    #     scheduledDepartureInterval: str
    #     scheduledDepartureTime: int
    #     scheduledTrack: str
    #     serviceDate: int
    #     situationIds: List[str]
    #     status: str
    #     stopId: str
    #     stopSequence: int
    #     totalStopsInTrip: int
    #     tripHeadsign: str
    #     tripId: str
    #     vehicleId: str
    #     tripStatus: "TripStatus" = None
    #     linked_references: bool = False
    #     references: "References" = None

    #     def __post_init__(self):
    #         if isinstance(self.scheduledArrivalTime, int):
    #             self.scheduledArrivalTime = DateTime(time=self.scheduledArrivalTime)
    #         if isinstance(self.scheduledDepartureTime, int):
    #         if self.tripStatus:
    #             self.tripStatus = TripStatus(**self.tripStatus)
    #         if self.linked_references:
    #             self.references = self.references

    #     __repr__ = generic_repr
    #     _repr_pretty_ = generic_repr_pretty
    @patch("onebusaway.client.requests.Session.get")
    def test_arrival_and_departure_for_stop(self, mock_get, client):
        mock_response = Mock()
        mock_response.json.return_value = {
            "data": {
                "entry": {
                    "actualTrack": "actualTrack1",
                    "arrivalEnabled": True,
                    "blockTripSequence": 1,
                    "departureEnabled": True,
                    "distanceFromStop": 0.1,
                    "frequency": "frequency1",
                    "historicalOccupancy": "historicalOccupancy1",
                    "lastUpdateTime": 1,
                    "numberOfStopsAway": 1,
                    "occupancyStatus": "occupancyStatus1",
                    "predicted": True,
                    "predictedArrivalInterval": "predictedArrivalInterval1",
                    "predictedArrivalTime": 1,
                    "predictedDepartureInterval": "predictedDepartureInterval1",
                    "predictedDepartureTime": 1,
                    "predictedOccupancy": "predictedOccupancy1",
                    "routeId": "route1",
                    "routeLongName": "Route 1",
                    "routeShortName": "R1",
                    "scheduledArrivalInterval": "scheduledArrivalInterval1",
                    "scheduledArrivalTime": 1,
                    "scheduledDepartureInterval": "scheduledDepartureInterval1",
                    "scheduledDepartureTime": 1,
                    "scheduledTrack": "scheduledTrack1",
                    "serviceDate": 1,
                    "situationIds": ["situation1"],
                    "status": "status1",
                    "stopId": "stop1",
                    "stopSequence": 1,
                    "totalStopsInTrip": 1,
                    "tripHeadsign": "Trip 1",
                    "tripId": "trip1",
                    "vehicleId": "vehicle1",
                }
            }
        }
        mock_get.return_value = mock_response
        arrival_and_departure = client.arrival_and_departure_for_stop(
            "stop1",
            "trip1",
            1,
            vehicleId="vehicle1",
            stopSequence=1,
            get_references=True,
        )
        assert arrival_and_departure.actualTrack == "actualTrack1"
        assert arrival_and_departure.arrivalEnabled is True
        assert arrival_and_departure.blockTripSequence == 1
        assert arrival_and_departure.departureEnabled is True
        assert arrival_and_departure.distanceFromStop == 0.1
        assert arrival_and_departure.frequency == "frequency1"
        assert arrival_and_departure.historicalOccupancy == "historicalOccupancy1"
        assert arrival_and_departure.lastUpdateTime == 1
        assert arrival_and_departure.numberOfStopsAway == 1
        assert arrival_and_departure.occupancyStatus == "occupancyStatus1"
        assert arrival_and_departure.predicted is True
        assert (
            arrival_and_departure.predictedArrivalInterval
            == "predictedArrivalInterval1"
        )
        assert arrival_and_departure.predictedArrivalTime.time == 1
        assert (
            arrival_and_departure.predictedDepartureInterval
            == "predictedDepartureInterval1"
        )
        assert arrival_and_departure.predictedDepartureTime.time == 1
        assert arrival_and_departure.predictedOccupancy == "predictedOccupancy1"
        assert arrival_and_departure.routeId == "route1"
        assert arrival_and_departure.routeLongName == "Route 1"
        assert arrival_and_departure.routeShortName == "R1"
        assert (
            arrival_and_departure.scheduledArrivalInterval
            == "scheduledArrivalInterval1"
        )
        assert arrival_and_departure.scheduledArrivalTime.time == 1

        assert (
            arrival_and_departure.scheduledDepartureInterval
            == "scheduledDepartureInterval1"
        )
        assert arrival_and_departure.scheduledDepartureTime.time == 1

        assert arrival_and_departure.scheduledTrack == "scheduledTrack1"
        assert (
            arrival_and_departure.predictedArrivalInterval
            == "predictedArrivalInterval1"
        )
        assert arrival_and_departure.predictedArrivalTime.time == 1
        assert (
            arrival_and_departure.predictedDepartureInterval
            == "predictedDepartureInterval1"
        )
        assert arrival_and_departure.predictedDepartureTime.time == 1
        assert arrival_and_departure.predictedOccupancy == "predictedOccupancy1"
        assert arrival_and_departure.routeId == "route1"
        assert arrival_and_departure.routeLongName == "Route 1"
        assert arrival_and_departure.routeShortName == "R1"
        assert (
            arrival_and_departure.scheduledArrivalInterval
            == "scheduledArrivalInterval1"
        )
        assert arrival_and_departure.scheduledArrivalTime.time == 1
        assert (
            arrival_and_departure.scheduledDepartureInterval
            == "scheduledDepartureInterval1"
        )
        assert arrival_and_departure.scheduledDepartureTime.time == 1
        assert arrival_and_departure.scheduledTrack == "scheduledTrack1"
        assert arrival_and_departure.serviceDate == 1
        assert arrival_and_departure.situationIds == ["situation1"]
        assert arrival_and_departure.status == "status1"
        assert arrival_and_departure.stopId == "stop1"
        assert arrival_and_departure.stopSequence == 1
        assert arrival_and_departure.totalStopsInTrip == 1
        assert arrival_and_departure.tripHeadsign == "Trip 1"
        assert arrival_and_departure.tripId == "trip1"
        assert arrival_and_departure.vehicleId == "vehicle1"
