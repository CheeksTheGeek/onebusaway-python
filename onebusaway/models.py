# models.py
from typing import List, Dict, Any, Tuple
from datetime import datetime

from .utils import generic_repr, generic_repr_pretty
from dataclasses import dataclass
from dataclasses import dataclass


@dataclass
class DateTime:
    time: int = None
    readableTime: str = None
    linked_references: bool = False
    references: "References" = None

    def __post_init__(self):
        if self.time is None and self.readableTime is None:
            raise ValueError(
                "At least one of 'time' or 'readableTime' must be provided."
            )
        if self.time is not None:
            self.unix_time = self.time
        if self.readableTime is not None:
            self.readableTime = datetime.strptime(
                self.readableTime, "%Y-%m-%dT%H:%M:%S%z"
            )
        if self.linked_references:
            self.references = References(**self.references)

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class Agency:
    agencyId: str
    lat: float
    lon: float
    latSpan: float
    lonSpan: float
    linked_references: bool = False
    references: "References" = None

    def __post_init__(self):
        if self.linked_references:
            self.references = References(**self.references)

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class AgencyDetails:
    disclaimer: str
    email: str
    fareUrl: str
    id: str
    lang: str
    name: str
    phone: str
    privateService: bool
    timezone: str
    url: str
    linked_references: bool = False
    references: "References" = None

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class ArrivalAndDeparture:
    actualTrack: str
    arrivalEnabled: bool
    blockTripSequence: int
    departureEnabled: bool
    distanceFromStop: float
    frequency: str
    historicalOccupancy: str
    lastUpdateTime: int
    numberOfStopsAway: int
    occupancyStatus: str
    predicted: bool
    predictedArrivalInterval: str
    predictedArrivalTime: int
    predictedDepartureInterval: str
    predictedDepartureTime: int
    predictedOccupancy: str
    routeId: str
    routeLongName: str
    routeShortName: str
    scheduledArrivalInterval: str
    scheduledArrivalTime: int
    scheduledDepartureInterval: str
    scheduledDepartureTime: int
    scheduledTrack: str
    serviceDate: int
    situationIds: List[str]
    status: str
    stopId: str
    stopSequence: int
    totalStopsInTrip: int
    tripHeadsign: str
    tripId: str
    vehicleId: str
    tripStatus: "TripStatus" = None
    linked_references: bool = False
    references: "References" = None

    def __post_init__(self):
        if isinstance(self.scheduledArrivalTime, int):
            self.scheduledArrivalTime = DateTime(time=self.scheduledArrivalTime)
        if isinstance(self.scheduledDepartureTime, int):
            self.scheduledDepartureTime = DateTime(time=self.scheduledDepartureTime)
        if isinstance(self.predictedArrivalTime, int):
            self.predictedArrivalTime = DateTime(time=self.predictedArrivalTime)
        if isinstance(self.predictedDepartureTime, int):
            self.predictedDepartureTime = DateTime(time=self.predictedDepartureTime)
        if self.tripStatus:
            self.tripStatus = TripStatus(**self.tripStatus)
        if self.linked_references:
            self.references = self.references

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class StopTime:
    stopId: str
    arrivalTime: int
    departureTime: int
    pickupType: int
    dropOffType: int

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class BlockStopTime:
    blockSequence: int
    distanceAlongBlock: float
    accumulatedSlackTime: int
    stopTime: StopTime

    def __post_init__(self):
        self.stopTime = StopTime(**self.stopTime)

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class BlockTrip:
    tripId: str
    blockStopTimes: List[BlockStopTime]
    accumulatedSlackTime: int
    distanceAlongBlock: float

    def __post_init__(self):
        self.blockStopTimes = [
            BlockStopTime(**stopTime) for stopTime in self.blockStopTimes
        ]

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class BlockConfiguration:
    activeServiceIds: List[str]
    inactiveServiceIds: List[str]
    trips: List[BlockTrip]

    def __post_init__(self):
        self.trips = [BlockTrip(**trip) for trip in self.trips]

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class Frequency:
    startTime: int
    endTime: int
    headway: int

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class ListResult:
    list: List
    limitExceeded: bool
    outOfRange: bool

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class Route:
    id: str
    shortName: str
    longName: str
    description: str
    type: int
    url: str
    color: str
    textColor: str
    agencyId: str
    nullSafeShortName: str

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class Call:
    stopId: str

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class VehicleJourney:
    lineId: str
    direction: int
    calls: List[Call]

    def __post_init__(self):
        self.calls = [Call(**call) for call in self.calls]

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class Affects:
    stops: List[str]
    vehicleJourneys: List[VehicleJourney]

    def __post_init__(self):
        self.vehicleJourneys = [
            VehicleJourney(**journey) for journey in self.vehicleJourneys
        ]

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class ConditionDetails:
    diversionPath: str
    diversionStopIds: List[str]

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class Consequences:
    condition: str
    conditionDetails: ConditionDetails

    def __post_init__(self):
        self.conditionDetails = ConditionDetails(**self.conditionDetails)

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class Situation:
    id: str
    creationTime: int
    environmentReason: str
    summary: str
    description: str
    affects: Affects
    consequences: Consequences

    def __post_init__(self):
        self.affects = Affects(**self.affects)
        self.consequences = Consequences(**self.consequences)

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class Stop:
    id: str
    lat: float
    lon: float
    direction: str
    name: str
    code: str
    locationType: int
    parent: str
    wheelchairBoarding: str
    routeIds: List[str]
    staticRouteIds: List[str]

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class Position:
    lat: float
    lon: float

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class ClosestStop:
    stopId: str
    distance: float

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class NextStop:
    stopId: str
    distance: float

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


# @dataclass
# class LastKnownLocation:
#     lat: float
#     lon: float

#     __repr__ = generic_repr
#     _repr_pretty_ = generic_repr_pretty


@dataclass
class TripStopTime:
    arrivalTime: int
    departureTime: int
    stopId: str
    distanceAlongTrip: float = None
    historicalOccupancy: str = None
    stopHeadsign: str = None
    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class Schedule:
    timeZone: str
    stopTimes: List[TripStopTime]
    previousTripId: str
    nextTripId: str
    frequency: Frequency = None

    def __post_init__(self):
        if self.stopTimes:
            self.stopTimes = [TripStopTime(**stopTime) for stopTime in self.stopTimes]
        if self.frequency:
            self.frequency = Frequency(**self.frequency)

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class TripStatus:
    activeTripId: str
    blockTripSequence: int
    serviceDate: int
    frequency: Frequency
    scheduledDistanceAlongTrip: float
    totalDistanceAlongTrip: float
    position: Position
    orientation: float
    closestStop: str
    closestStopTimeOffset: int
    nextStop: str
    nextStopTimeOffset: int
    occupancyStatus: str
    phase: str
    status: str
    predicted: bool
    lastUpdateTime: int
    lastLocationUpdateTime: int
    lastKnownDistanceAlongTrip: float
    lastKnownOrientation: float
    distanceAlongTrip: float
    scheduleDeviation: int
    vehicleId: str
    lastKnownLocation: Position = None
    occupancyCount: int = None
    occupancyCapacity: int = None
    situationIds: List[str] = None

    def __post_init__(self):
        if self.position:
            self.position = Position(**self.position)
        if self.lastKnownLocation:
            self.lastKnownLocation = Position(**self.lastKnownLocation)

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class TripDetails:
    tripId: str
    serviceDate: int
    frequency: Frequency
    situationIds: List[str]
    status: TripStatus = None
    schedule: Schedule = None

    def __post_init__(self):
        if self.status:
            self.status = TripStatus(**self.status)
        if self.schedule:
            self.schedule = Schedule(**self.schedule)

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class Trip:
    id: str
    routeId: str
    tripShortName: str
    tripHeadsign: str
    serviceId: str
    shapeId: str
    directionId: int
    blockId: str
    timeZone: str
    routeShortName: str
    peakOffpeak: int
    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class TripReference:
    blockId: str
    directionId: str
    id: str
    peakOffpeak: int
    routeId: str
    routeShortName: str
    serviceId: str
    shapeId: str
    timeZone: str
    tripHeadsign: str
    tripShortName: str
    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class VehicleStatus:
    lastLocationUpdateTime: int
    lastUpdateTime: int
    occupancyCapacity: int
    occupancyCount: int
    occupancyStatus: str
    phase: str
    status: str
    tripId: str
    vehicleId: str
    location: Position = None
    tripStatus: TripStatus = None

    def __post_init__(self):
        if self.tripStatus:
            self.tripStatus = TripStatus(**self.tripStatus)
        if self.location:
            self.location = Position(**self.location)

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class References:
    agencies: List[AgencyDetails]
    routes: List[Route]
    stops: List[Stop]
    trips: List[TripReference]
    situations: List[Situation]
    stopTimes: List[TripStopTime] = None

    def __post_init__(self):
        self.agencies = [AgencyDetails(**agency) for agency in self.agencies]
        self.routes = [Route(**route) for route in self.routes]
        self.stops = [Stop(**stop) for stop in self.stops]
        self.trips = [TripReference(**trip) for trip in self.trips]
        self.situations = [Situation(**situation) for situation in self.situations]
        if self.stopTimes:
            self.stopTimes = [TripStopTime(**stopTime) for stopTime in self.stopTimes]

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class Response:
    version: int = None
    code: int = None
    text: str = ""
    currentTime: int = None
    data: Dict[str, Any] = None

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty

    def to_dict(self):
        return {
            "version": self.version,
            "code": self.code,
            "text": self.text,
            "currentTime": self.currentTime,
            "data": self.data,
        }


@dataclass
class StopWithArrivalsAndDepartures:
    stopId: str
    arrivalsAndDepartures: List[ArrivalAndDeparture]
    nearbyStopIds: List[str]
    situationIds: List[str]
    linked_references: bool = False
    references: "References" = None

    def __post_init__(self):
        self.arrivalsAndDepartures = [
            ArrivalAndDeparture(**arrivalAndDeparture)
            for arrivalAndDeparture in self.arrivalsAndDepartures
        ]
        if self.linked_references:
            self.references = self.references

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class Block:
    id: str
    configurations: List[BlockConfiguration]
    linked_references: bool = False
    references: "References" = None

    def __post_init__(self):
        self.configurations = [
            BlockConfiguration(**configuration) for configuration in self.configurations
        ]
        if self.linked_references:
            self.references = self.references

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class StopTripGrouping:
    directionId: int
    tripHeadsign: str
    stopIds: List[str]
    tripIds: List[str]
    tripsWithStopTimes: List[TripStopTime]

    def __post_init__(self):
        self.tripsWithStopTimes = [
            TripStopTime(**tripStopTime) for tripStopTime in self.tripsWithStopTimes
        ]

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class RouteSchedule:
    routeId: Tuple[str, str]
    serviceIds: List[str]
    scheduleDate: int
    stopTripGroupings: List[StopTripGrouping]

    def __post_init__(self):
        self.routeId = self.routeId.split("_")
        self.stopTripGroupings = [
            StopTripGrouping(**grouping) for grouping in self.stopTripGroupings
        ]

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class EncodedPolyline:
    points: str
    length: int
    levels: str = None

    def __post_init__(self):
        self.points = self.decode_polyline(self.points)

    def decode_polyline(self, polyline_str: str) -> List[Tuple[float, float]]:
        index, lat, lng = 0, 0, 0
        coordinates: List[Tuple[float, float]] = []
        while index < len(polyline_str):
            b, shift, result = 0, 0, 0
            while True:
                b = ord(polyline_str[index]) - 63
                index += 1
                result |= (b & 0x1F) << shift
                shift += 5
                if b < 0x20:
                    break
            dlat = ~(result >> 1) if result & 1 else result >> 1
            lat += dlat
            shift, result = 0, 0
            while True:
                b = ord(polyline_str[index]) - 63
                index += 1
                result |= (b & 0x1F) << shift
                shift += 5
                if b < 0x20:
                    break
            dlng = ~(result >> 1) if result & 1 else result >> 1
            lng += dlng
            coordinates.append((lat / 1e5, lng / 1e5))
        return coordinates

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class StopGroup:
    id: int
    name: str
    stopIds: List[str]
    polylines: List[EncodedPolyline]

    def __post_init__(self):
        self.polylines = [EncodedPolyline(**polyline) for polyline in self.polylines]

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class StopGrouping:
    type: str
    ordered: bool
    stopGroups: List[StopGroup]

    def __post_init__(self):
        self.stopGroups = [StopGroup(**group) for group in self.stopGroups]

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class StopsForRoute:
    routeId: str
    stopIds: List[str]
    stopGroupings: List[StopGrouping]
    polylines: List[EncodedPolyline]

    def __post_init__(self):
        self.routeId: Tuple[str, str] = self.routeId.split("_")
        self.polylines = [EncodedPolyline(**polyline) for polyline in self.polylines]

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class ScheduleStopTime:
    arrivalTime: int
    departureTime: int
    tripId: str
    serviceId: str
    arrivalEnabled: bool
    departureEnabled: bool
    stopHeadsign: str

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class StopRouteDirectionSchedule:
    tripHeadsign: str
    scheduleStopTimes: List[ScheduleStopTime]
    scheduleFrequencies: List[Frequency] = None

    def __post_init__(self):
        self.scheduleStopTimes = [
            ScheduleStopTime(**stopTime) for stopTime in self.scheduleStopTimes
        ]
        if self.scheduleFrequencies:
            self.scheduleFrequencies = [
                Frequency(**frequency) for frequency in self.scheduleFrequencies
            ]

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class StopRouteSchedule:
    routeId: Tuple[str, str]
    stopRouteDirectionSchedules: List[StopRouteDirectionSchedule]

    def __post_init__(self):
        self.routeId = self.routeId.split("_")
        self.stopRouteDirectionSchedules = [
            StopRouteDirectionSchedule(**directionSchedule)
            for directionSchedule in self.stopRouteDirectionSchedules
        ]

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class StopCalendarDay:
    date: int
    group: int
    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty


@dataclass
class StopSchedule:
    date: int
    stopId: str
    stopRouteSchedules: List[StopRouteSchedule]
    timeZone: str = "America/Los_Angeles"
    stopCalendarDays: List[StopCalendarDay] = None

    def __post_init__(self):
        self.stopRouteSchedules = [
            StopRouteSchedule(**routeSchedule)
            for routeSchedule in self.stopRouteSchedules
        ]
        if self.stopCalendarDays:
            self.stopCalendarDays = [
                StopCalendarDay(**calendarDay) for calendarDay in self.stopCalendarDays
            ]

    __repr__ = generic_repr
    _repr_pretty_ = generic_repr_pretty
