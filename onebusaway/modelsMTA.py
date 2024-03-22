from typing import List, Dict, Any, Tuple


def generic_repr(self):
    attributes = ", ".join(f"{key}={value!r}" for key, value in self.__dict__.items())
    return f"{self.__class__.__name__}({attributes})"


class Agency:
    def __init__(
        self,
        agencyId: str,
        lat: float,
        lon: float,
        latSpan: float,
        lonSpan: float,
    ):
        self.agencyId = agencyId
        self.lat = lat
        self.lon = lon
        self.latSpan = latSpan
        self.lonSpan = lonSpan


class ArrivalAndDeparture:
    def __init__(
        self,
        routeId: str,
        tripId: str,
        serviceDate: int,
        stopId: str,
        stopSequence: int,
        totalStopsInTrip: int,
        blockTripSequence: int,
        routeShortName: str,
        routeLongName: str,
        tripHeadsign: str,
        arrivalEnabled: bool,
        departureEnabled: bool,
        scheduledArrivalTime: int,
        scheduledDepartureTime: int,
        frequency: str,
        predicted: bool,
        predictedArrivalTime: int,
        predictedDepartureTime: int,
        distanceFromStop: float,
        numberOfStopsAway: int,
        tripStatus: str,
    ):
        self.routeId = routeId
        self.tripId = tripId
        self.serviceDate = serviceDate
        self.stopId = stopId
        self.stopSequence = stopSequence
        self.totalStopsInTrip = totalStopsInTrip
        self.blockTripSequence = blockTripSequence
        self.routeShortName = routeShortName
        self.routeLongName = routeLongName
        self.tripHeadsign = tripHeadsign
        self.arrivalEnabled = arrivalEnabled
        self.departureEnabled = departureEnabled
        self.scheduledArrivalTime = scheduledArrivalTime
        self.scheduledDepartureTime = scheduledDepartureTime
        self.frequency = frequency
        self.predicted = predicted
        self.predictedArrivalTime = predictedArrivalTime
        self.predictedDepartureTime = predictedDepartureTime
        self.distanceFromStop = distanceFromStop
        self.numberOfStopsAway = numberOfStopsAway
        self.tripStatus = tripStatus

    __repr__ = generic_repr


class StopTime:
    def __init__(
        self,
        stopId: str,
        arrivalTime: int,
        departureTime: int,
        pickupType: int,
        dropOffType: int,
    ):
        self.stopId = stopId
        self.arrivalTime = arrivalTime
        self.departureTime = departureTime
        self.pickupType = pickupType
        self.dropOffType = dropOffType


class BlockStopTime:
    def __init__(
        self,
        blockSequence: int,
        distanceAlongBlock: float,
        accumulatedSlackTime: int,
        stopTime: StopTime,
    ):
        self.blockSequence = blockSequence
        self.distanceAlongBlock = distanceAlongBlock
        self.accumulatedSlackTime = accumulatedSlackTime
        self.stopTime = stopTime


class BlockTrip:
    def __init__(
        self,
        tripId: str,
        blockStopTimes: List[BlockStopTime],
        accumulatedSlackTime: int,
        distanceAlongBlock: float,
    ):
        self.tripId = tripId
        self.blockStopTimes = blockStopTimes
        self.accumulatedSlackTime = accumulatedSlackTime
        self.distanceAlongBlock = distanceAlongBlock


class BlockConfiguration:
    def __init__(
        self,
        activeServiceIds: List[str],
        inactiveServiceIds: List[str],
        trips: List[BlockTrip],
    ):
        self.activeServiceIds = activeServiceIds
        self.inactiveServiceIds = inactiveServiceIds
        self.trips = trips


class Frequency:
    def __init__(self, startTime: int, endTime: int, headway: int):
        self.startTime = startTime
        self.endTime = endTime
        self.headway = headway


class ListResult:
    def __init__(self, list: List, limitExceeded: bool, outOfRange: bool):
        self.list = list
        self.limitExceeded = limitExceeded
        self.outOfRange = outOfRange


class Route:
    def __init__(
        self,
        id: str,
        shortName: str,
        longName: str,
        description: str,
        type: int,
        url: str,
        color: str,
        textColor: str,
        agencyId: str,
    ):
        self.id = id
        self.shortName = shortName
        self.longName = longName
        self.description = description
        self.type = type
        self.url = url
        self.color = color
        self.textColor = textColor
        self.agencyId = agencyId


class Call:
    def __init__(self, stopId: str):
        self.stopId = stopId


class VehicleJourney:
    def __init__(self, lineId: str, direction: int, calls: List[Call]):
        self.lineId = lineId
        self.direction = direction
        self.calls = calls


class Affects:
    def __init__(self, stops: List[str], vehicleJourneys: List[VehicleJourney]):
        self.stops = stops
        self.vehicleJourneys = vehicleJourneys


class ConditionDetails:
    def __init__(self, diversionPath: str, diversionStopIds: List[str]):
        self.diversionPath = diversionPath
        self.diversionStopIds = diversionStopIds


class Consequences:
    def __init__(self, condition: str, conditionDetails: ConditionDetails):
        self.condition = condition
        self.conditionDetails = conditionDetails


class Situation:
    def __init__(
        self,
        id: str,
        creationTime: int,
        environmentReason: str,
        summary: str,
        description: str,
        affects: Affects,
        consequences: Consequences,
    ):
        self.id = id
        self.creationTime = creationTime
        self.environmentReason = environmentReason
        self.summary = summary
        self.description = description
        self.affects = affects
        self.consequences = consequences


class Stop:
    def __init__(
        self,
        id: str,
        lat: float,
        lon: float,
        direction: str,
        name: str,
        code: str,
        locationType: int,
        wheelchairBoarding: str,
        routeIds: List[str],
    ):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.direction = direction
        self.name = name
        self.code = code
        self.locationType = locationType
        self.wheelchairBoarding = wheelchairBoarding
        self.routeIds = routeIds


class Position:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon


class ClosestStop:
    def __init__(self, stopId: str, distance: float):
        self.stopId = stopId
        self.distance = distance


class NextStop:
    def __init__(self, stopId: str, distance: float):
        self.stopId = stopId
        self.distance = distance


class LastKnownLocation:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon


class TripStopTime:
    def __init__(self, arrivalTime: int, departureTime: int, stopId: str):
        self.arrivalTime = arrivalTime
        self.departureTime = departureTime
        self.stopId = stopId


class Schedule:
    def __init__(
        self,
        timeZone: str,
        stopTimes: List[TripStopTime],
        previousTripId: str,
        nextTripId: str,
    ):
        self.timeZone = timeZone
        self.stopTimes = stopTimes
        self.previousTripId = previousTripId
        self.nextTripId = nextTripId


class TripStatus:
    def __init__(
        self,
        activeTripId: str,
        blockTripSequence: int,
        serviceDate: int,
        frequency: Frequency,
        scheduledDistanceAlongTrip: float,
        totalDistanceAlongTrip: float,
        position: Position,
        orientation: float,
        closestStop: str,
        closestStopTimeOffset: int,
        nextStop: str,
        nextStopTimeOffset: int,
        occupancyStatus: str,
        phase: str,
        status: str,
        predicted: bool,
        lastUpdateTime: int,
        lastLocationUpdateTime: int,
        lastKnownLocation: LastKnownLocation,
        lastKnownDistanceAlongTrip: float,
        lastKnownOrientation: float,
        distanceAlongTrip: float,
        scheduleDeviation: int,
        vehicleId: str,
    ):
        self.activeTripId = activeTripId
        self.blockTripSequence = blockTripSequence
        self.serviceDate = serviceDate
        self.frequency = frequency
        self.scheduledDistanceAlongTrip = scheduledDistanceAlongTrip
        self.totalDistanceAlongTrip = totalDistanceAlongTrip
        self.position = position
        self.orientation = orientation
        self.closestStop = closestStop
        self.closestStopTimeOffset = closestStopTimeOffset
        self.nextStop = nextStop
        self.nextStopTimeOffset = nextStopTimeOffset
        self.occupancyStatus = occupancyStatus
        self.phase = phase
        self.status = status
        self.predicted = predicted
        self.lastUpdateTime = lastUpdateTime
        self.lastLocationUpdateTime = lastLocationUpdateTime
        self.lastKnownLocation = lastKnownLocation
        self.lastKnownDistanceAlongTrip = lastKnownDistanceAlongTrip
        self.lastKnownOrientation = lastKnownOrientation
        self.distanceAlongTrip = distanceAlongTrip
        self.scheduleDeviation = scheduleDeviation
        self.vehicleId = vehicleId


class TripDetails:
    def __init__(
        self,
        tripId: str,
        serviceDate: int,
        frequency: Frequency,
        status: TripStatus,
        schedule: Schedule,
        situationIds: List[str],
    ):
        self.tripId = tripId
        self.serviceDate = serviceDate
        self.frequency = frequency
        self.status = status
        self.schedule = schedule
        self.situationIds = situationIds


class Trip:
    def __init__(
        self,
        id: str,
        routeId: str,
        tripShortName: str,
        tripHeadsign: str,
        serviceId: str,
        shapeId: str,
        directionId: int,
    ):
        self.id = id
        self.routeId = routeId
        self.tripShortName = tripShortName
        self.tripHeadsign = tripHeadsign
        self.serviceId = serviceId
        self.shapeId = shapeId
        self.directionId = directionId


class VehicleStatus:
    def __init__(
        self,
        vehicleId: str,
        lastUpdateTime: int,
        lastLocationUpdateTime: int,
        location: Position,
        tripId: str,
        tripStatus: TripStatus,
    ):
        self.vehicleId = vehicleId
        self.lastUpdateTime = lastUpdateTime
        self.lastLocationUpdateTime = lastLocationUpdateTime
        self.location = location
        self.tripId = tripId
        self.tripStatus = tripStatus


class References:
    def __init__(
        self,
        agencies: List[Agency],
        routes: List[Route],
        stops: List[Stop],
        trips: List[Trip],
        situations: List[Situation],
    ):
        self.agencies = agencies
        self.routes = routes
        self.stops = stops
        self.trips = trips
        self.situations = situations


class Response:
    def __init__(
        self,
        version: int,
        code: int,
        text: str,
        currentTime: int,
        data: Dict[str, Any],
    ):
        self.version = version
        self.code = code
        self.text = text
        self.currentTime = currentTime
        self.data = data

    def __repr__(self):
        return f"Response(version={self.version}, code={self.code}, text={self.text}, currentTime={self.currentTime}, data={self.data})"

    def to_dict(self):
        return {
            "version": self.version,
            "code": self.code,
            "text": self.text,
            "currentTime": self.currentTime,
            "data": self.data,
        }


class StopWithArrivalsAndDepartures:
    def __init__(
        self,
        stopId: str,
        arrivalsAndDepartures: List[ArrivalAndDeparture],
        nearbyStopIds: List[str],
        situationIds: List[str],
    ):
        self.stopId = stopId
        self.arrivalsAndDepartures = arrivalsAndDepartures
        self.nearbyStopIds = nearbyStopIds
        self.situationIds = situationIds


class Block:
    def __init__(self, id: str, configurations: List[BlockConfiguration]):
        self.id = id
        self.configurations = configurations


class StopTripGrouping:
    def __init__(
        self,
        directionId: int,
        tripHeadsign: str,
        stopIds: List[str],
        tripIds: List[str],
        tripsWithStopTimes: List[TripStopTime],
    ):
        self.directionId = directionId
        self.tripHeadsign = tripHeadsign
        self.stopIds = stopIds
        self.tripIds = tripIds
        self.tripsWithStopTimes = tripsWithStopTimes


class RouteSchedule:
    def __init__(
        self,
        routeId: str,
        serviceIds: List[str],
        scheduleDate: int,
        stopTripGroupings: List[StopTripGrouping],
    ):
        self.routeId: Tuple[str, str] = routeId.split("_")
        self.serviceIds = serviceIds
        self.scheduleDate = scheduleDate
        self.stopTripGroupings = stopTripGroupings


class EncodedPolyline:
    def __init__(self, points: str, length: int):
        self.points = points
        self.length = length

    @property
    def coordinates(self, polyline_str) -> List[Tuple[float, float]]:
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


class StopGroup:
    def __init__(
        self, id: int, name: str, stopIds: List[str], polylines: List[EncodedPolyline]
    ):
        self.id = id
        self.name = name
        self.stopIds = stopIds
        self.polylines = polylines


class StopGrouping:
    def __init__(self, type: str, ordered: bool, stopGroups: List[StopGroup]):
        self.type = type
        self.ordered = ordered
        self.stopGroups = stopGroups


class StopsForRoute:
    def __init__(
        self,
        routeId: str,
        stopIds: List[str],
        stopGroupings: List[StopGrouping],
        polylines: List[EncodedPolyline],
    ):
        self.routeId: Tuple[str, str] = routeId.split("_")
        self.stopIds = stopIds
        self.stopGroupings = stopGroupings
        self.polylines = polylines


class ScheduleStopTime:
    def __init__(
        self, arrivalTime: int, departureTime: int, tripId: str, serviceId: str
    ):
        self.arrivalTime = arrivalTime
        self.departureTime = departureTime
        self.tripId = tripId
        self.serviceId = serviceId


class StopRouteDirectionSchedule:
    def __init__(self, tripHeadsign: str, scheduleStopTimes: List[ScheduleStopTime]):
        self.tripHeadsign = tripHeadsign
        self.scheduleStopTimes = scheduleStopTimes


class StopRouteSchedule:
    def __init__(
        self,
        routeId: str,
        stopRouteDirectionSchedules: List[StopRouteDirectionSchedule],
    ):
        self.routeId: Tuple[str, str] = routeId.split("_")
        self.stopRouteDirectionSchedules = stopRouteDirectionSchedules


class StopCalendarDay:
    def __init__(self, date: int, group: int):
        self.date = date
        self.group = group


class StopSchedule:
    def __init__(
        self,
        date: int,
        stopId: str,
        stopRouteSchedules: List[StopRouteSchedule],
        timeZone: str,
        stopCalendarDays: List[StopCalendarDay],
    ):
        self.date = date
        self.stopId = stopId
        self.stopRouteSchedules = stopRouteSchedules
        self.timeZone = timeZone
        self.stopCalendarDays = stopCalendarDays
