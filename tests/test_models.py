# test_models.py
import pytest
from datetime import datetime
from onebusaway.models import (
    Agency,
    AgencyDetails,
    ArrivalAndDeparture,
    DateTime,
    References,
    Route,
    Stop,
    TripDetails,
    TripStatus,
    Position,
    Schedule,
    TripStopTime,
)


def test_agency():
    agency = Agency(
        agencyId="agency1", lat=47.6097, lon=-122.3331, latSpan=0.1, lonSpan=0.2
    )
    assert agency.agencyId == "agency1"
    assert agency.lat == 47.6097
    assert agency.lon == -122.3331
    assert agency.latSpan == 0.1
    assert agency.lonSpan == 0.2


def test_agency_details():
    agency_details = AgencyDetails(
        disclaimer="Disclaimer text",
        email="info@agency.com",
        fareUrl="https://agency.com/fares",
        id="agency1",
        lang="en",
        name="Agency One",
        phone="555-1234",
        privateService=False,
        timezone="America/Los_Angeles",
        url="https://agency.com",
    )
    assert agency_details.disclaimer == "Disclaimer text"
    assert agency_details.email == "info@agency.com"
    assert agency_details.fareUrl == "https://agency.com/fares"
    assert agency_details.id == "agency1"
    assert agency_details.lang == "en"
    assert agency_details.name == "Agency One"
    assert agency_details.phone == "555-1234"
    assert agency_details.privateService is False
    assert agency_details.timezone == "America/Los_Angeles"
    assert agency_details.url == "https://agency.com"


def test_arrival_and_departure():
    arrival_and_departure = ArrivalAndDeparture(
        actualTrack="1",
        arrivalEnabled=True,
        blockTripSequence=1,
        departureEnabled=True,
        distanceFromStop=0.1,
        frequency="15min",
        historicalOccupancy="MANY_SEATS_AVAILABLE",
        lastUpdateTime=1683844800,
        numberOfStopsAway=2,
        occupancyStatus="MANY_SEATS_AVAILABLE",
        predicted=True,
        predictedArrivalInterval="15min",
        predictedArrivalTime=1683845100,
        predictedDepartureInterval="15min",
        predictedDepartureTime=1683845400,
        predictedOccupancy="MANY_SEATS_AVAILABLE",
        routeId="route1",
        routeLongName="Route One",
        routeShortName="1",
        scheduledArrivalInterval="15min",
        scheduledArrivalTime=1683845100,
        scheduledDepartureInterval="15min",
        scheduledDepartureTime=1683845400,
        scheduledTrack="1",
        serviceDate=20230511,
        situationIds=[],
        status="SCHEDULED",
        stopId="stop1",
        stopSequence=5,
        totalStopsInTrip=10,
        tripHeadsign="Downtown",
        tripId="trip1",
        vehicleId="vehicle1",
    )
    assert arrival_and_departure.actualTrack == "1"
    assert arrival_and_departure.arrivalEnabled is True
    assert arrival_and_departure.blockTripSequence == 1
    assert arrival_and_departure.departureEnabled is True
    assert arrival_and_departure.distanceFromStop == 0.1
    assert arrival_and_departure.frequency == "15min"
    assert arrival_and_departure.historicalOccupancy == "MANY_SEATS_AVAILABLE"
    assert arrival_and_departure.lastUpdateTime == 1683844800
    assert arrival_and_departure.numberOfStopsAway == 2
    assert arrival_and_departure.occupancyStatus == "MANY_SEATS_AVAILABLE"
    assert arrival_and_departure.predicted is True
    assert arrival_and_departure.predictedArrivalInterval == "15min"
    assert arrival_and_departure.predictedArrivalTime.time == 1683845100
    assert arrival_and_departure.predictedDepartureInterval == "15min"
    assert arrival_and_departure.predictedDepartureTime.time == 1683845400
    assert arrival_and_departure.predictedOccupancy == "MANY_SEATS_AVAILABLE"
    assert arrival_and_departure.routeId == "route1"
    assert arrival_and_departure.routeLongName == "Route One"
    assert arrival_and_departure.routeShortName == "1"
    assert arrival_and_departure.scheduledArrivalInterval == "15min"
    assert arrival_and_departure.scheduledArrivalTime.time == 1683845100
    assert arrival_and_departure.scheduledDepartureInterval == "15min"
    assert arrival_and_departure.scheduledDepartureTime.time == 1683845400
    assert arrival_and_departure.scheduledTrack == "1"
    assert arrival_and_departure.serviceDate == 20230511
    assert arrival_and_departure.situationIds == []
    assert arrival_and_departure.status == "SCHEDULED"
    assert arrival_and_departure.stopId == "stop1"
    assert arrival_and_departure.stopSequence == 5
    assert arrival_and_departure.totalStopsInTrip == 10
    assert arrival_and_departure.tripHeadsign == "Downtown"
    assert arrival_and_departure.tripId == "trip1"
    assert arrival_and_departure.vehicleId == "vehicle1"


def test_date_time():
    # "%Y-%m-%dT%H:%M:%S%z"
    date_time = DateTime(time=1683844800, readableTime="2023-05-11T12:00:00-0700")
    assert date_time.time == 1683844800
    assert date_time.readableTime == datetime.strptime(
        "2023-05-11T12:00:00-0700", "%Y-%m-%dT%H:%M:%S%z"
    )


def test_references():
    references = References(
        agencies=[
            {
                "disclaimer": "Disclaimer text",
                "email": "info@agency.com",
                "fareUrl": "https://agency.com/fares",
                "id": "agency1",
                "lang": "en",
                "name": "Agency One",
                "phone": "555-1234",
                "privateService": False,
                "timezone": "America/Los_Angeles",
                "url": "https://agency.com",
            }
        ],
        routes=[
            {
                "id": "route1",
                "shortName": "1",
                "longName": "Route One",
                "description": "Route One description",
                "type": 3,
                "url": "https://agency.com/route1",
                "color": "FF0000",
                "textColor": "000000",
                "agencyId": "agency1",
                "nullSafeShortName": "1",
            }
        ],
        stops=[
            {
                "id": "stop1",
                "lat": 47.6097,
                "lon": -122.3331,
                "direction": "N",
                "name": "Stop One",
                "code": "1",
                "locationType": 0,
                "parent": None,
                "wheelchairBoarding": "UNKNOWN",
                "routeIds": ["route1", "route2"],
                "staticRouteIds": ["route1", "route2"],
            }
        ],
        trips=[],
        situations=[],
    )
    assert len(references.agencies) == 1
    assert references.agencies[0].id == "agency1"
    assert references.agencies[0].name == "Agency One"
    assert references.agencies[0].url == "https://agency.com"
    assert len(references.routes) == 1
    assert references.routes[0].id == "route1"
    assert references.routes[0].shortName == "1"
    assert references.routes[0].longName == "Route One"
    assert references.routes[0].agencyId == "agency1"
    assert len(references.stops) == 1
    assert references.stops[0].id == "stop1"
    assert references.stops[0].lat == 47.6097
    assert references.stops[0].lon == -122.3331
    assert references.stops[0].name == "Stop One"
    assert references.stops[0].code == "1"
    assert references.stops[0].locationType == 0
    assert references.stops[0].routeIds == ["route1", "route2"]
    assert len(references.situations) == 0


def test_route():
    route = Route(
        id="route1",
        shortName="1",
        longName="Route One",
        description="Route One description",
        type=3,
        url="https://agency.com/route1",
        color="FF0000",
        textColor="000000",
        agencyId="agency1",
        nullSafeShortName="1",
    )
    assert route.id == "route1"
    assert route.shortName == "1"
    assert route.longName == "Route One"
    assert route.description == "Route One description"
    assert route.type == 3
    assert route.url == "https://agency.com/route1"
    assert route.color == "FF0000"
    assert route.textColor == "000000"
    assert route.agencyId == "agency1"
    assert route.nullSafeShortName == "1"


def test_stop():
    stop = Stop(
        id="stop1",
        lat=47.6097,
        lon=-122.3331,
        direction="N",
        name="Stop One",
        code="1",
        locationType=0,
        parent=None,
        wheelchairBoarding="UNKNOWN",
        routeIds=["route1", "route2"],
        staticRouteIds=["route1", "route2"],
    )
    assert stop.id == "stop1"
    assert stop.lat == 47.6097
    assert stop.lon == -122.3331
    assert stop.direction == "N"
    assert stop.name == "Stop One"
    assert stop.code == "1"
    assert stop.locationType == 0
    assert stop.parent is None
    assert stop.wheelchairBoarding == "UNKNOWN"
    assert stop.routeIds == ["route1", "route2"]
    assert stop.staticRouteIds == ["route1", "route2"]


def test_trip_details():
    trip_details = TripDetails(
        tripId="trip1",
        serviceDate=20230511,
        frequency=None,
        situationIds=[],
        status=TripStatus(
            activeTripId="trip1",
            blockTripSequence=1,
            serviceDate=20230511,
            frequency=None,
            scheduledDistanceAlongTrip=0.5,
            totalDistanceAlongTrip=10.0,
            position=Position(lat=47.6097, lon=-122.3331),
            orientation=90.0,
            closestStop="stop1",
            closestStopTimeOffset=120,
            nextStop="stop2",
            nextStopTimeOffset=300,
            occupancyStatus="MANY_SEATS_AVAILABLE",
            phase="IN_PROGRESS",
            status="STARTED",
            predicted=True,
            lastUpdateTime=1683844800,
            lastLocationUpdateTime=1683844700,
            lastKnownDistanceAlongTrip=0.6,
            lastKnownOrientation=85.0,
            distanceAlongTrip=0.7,
            scheduleDeviation=60,
            vehicleId="vehicle1",
            lastKnownLocation=None,
            occupancyCount=None,
            occupancyCapacity=None,
            situationIds=None,
        ),
        schedule=Schedule(
            timeZone="America/Los_Angeles",
            stopTimes=[
                TripStopTime(
                    arrivalTime=1683844800,
                    departureTime=1683845400,
                    stopId="stop1",
                    distanceAlongTrip=0.5,
                    historicalOccupancy="MANY_SEATS_AVAILABLE",
                    stopHeadsign="Downtown",
                )
            ],
            previousTripId="trip0",
            nextTripId="trip2",
            frequency=None,
        ),
    )
    assert trip_details.tripId == "trip1"
    assert trip_details.serviceDate == 20230511
    assert trip_details.frequency is None
    assert trip_details.situationIds == []
    assert trip_details.status.activeTripId == "trip1"
    assert trip_details.status.blockTripSequence == 1
    assert trip_details.status.serviceDate == 20230511
    assert trip_details.status.frequency is None
    assert trip_details.status.scheduledDistanceAlongTrip == 0.5
    assert trip_details.status.totalDistanceAlongTrip == 10.0
    assert trip_details.status.position.lat == 47.6097
    assert trip_details.status.position.lon == -122.3331
    assert trip_details.status.orientation == 90.0
    assert trip_details.status.closestStop == "stop1"
    assert trip_details.status.closestStopTimeOffset == 120
    assert trip_details.status.nextStop == "stop2"
    assert trip_details.status.nextStopTimeOffset == 300
    assert trip_details.status.occupancyStatus == "MANY_SEATS_AVAILABLE"
    assert trip_details.status.phase == "IN_PROGRESS"
    assert trip_details.status.status == "STARTED"
    assert trip_details.status.predicted is True
    assert trip_details.status.lastUpdateTime == 1683844800
    assert trip_details.status.lastLocationUpdateTime == 1683844700
    assert trip_details.status.lastKnownDistanceAlongTrip == 0.6
    assert trip_details.status.lastKnownOrientation == 85.0
    assert trip_details.status.distanceAlongTrip == 0.7
    assert trip_details.status.scheduleDeviation == 60
    assert trip_details.status.vehicleId == "vehicle1"
    assert trip_details.status.lastKnownLocation is None
    assert trip_details.status.occupancyCount is None
    assert trip_details.status.occupancyCapacity is None
    assert trip_details.status.situationIds is None
    assert trip_details.schedule.timeZone == "America/Los_Angeles"
    assert len(trip_details.schedule.stopTimes) == 1
    assert trip_details.schedule.stopTimes[0].arrivalTime == 1683844800
    assert trip_details.schedule.stopTimes[0].departureTime == 1683845400
    assert trip_details.schedule.stopTimes[0].stopId == "stop1"
    assert trip_details.schedule.stopTimes[0].distanceAlongTrip == 0.5
    assert (
        trip_details.schedule.stopTimes[0].historicalOccupancy == "MANY_SEATS_AVAILABLE"
    )
    assert trip_details.schedule.stopTimes[0].stopHeadsign == "Downtown"
    assert trip_details.schedule.previousTripId == "trip0"
    assert trip_details.schedule.nextTripId == "trip2"
    assert trip_details.schedule.frequency is None
