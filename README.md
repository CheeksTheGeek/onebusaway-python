# OneBusAway Python Client

[![PyPI version](https://img.shields.io/pypi/v/onebusaway.svg)](https://pypi.org/project/onebusaway/)
[![PyPI downloads](https://img.shields.io/pypi/dm/onebusaway.svg)](https://pypi.org/project/onebusaway/)
[![License](https://img.shields.io/pypi/l/onebusaway.svg)](https://pypi.org/project/onebusaway/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The OneBusAway Python Client is a Python library for interacting with the [OneBusAway API](https://onebusaway.org/). It provides a simple and convenient way to access real-time transit data, schedules, and other information from various transit agencies.

## Features

- **Comprehensive API Coverage**: Access a wide range of endpoints for retrieving transit data, including agency information, routes, stops, arrivals and departures, trip details, vehicle locations, and more.
- **Flexible Usage**: Use the library in both synchronous and asynchronous modes, making it suitable for various application types, including web applications, scripts, and data analysis tasks.
- **Easy Integration**: The library is designed to be intuitive and easy to use, with a straightforward API and comprehensive documentation.
- **Robust Error Handling**: Enjoy robust error handling with custom exceptions for common API errors, such as missing or invalid API keys, bad requests, and more.
- **Well-Tested**: The library is thoroughly tested, ensuring reliable and consistent behavior across different scenarios.

## Installation

You can install the OneBusAway Python Client using pip:

```
pip install onebusaway
```

## Getting Started

Follow these steps to get started with the OneBusAway Python Client:

1. **Obtain an API Key**: To use the OneBusAway API, you'll need to obtain an API key. Visit the [OneBusAway Developers](https://developers.onebusaway.org/) website to sign up and get your API key.

2. **Set the API Key**: Set the `OBA_API_KEY` environment variable with your API key:

```
export OBA_API_KEY=your_api_key
```

3. **Import the Client**: Import the `OneBusAway` class from the library:

```python
from onebusaway import OneBusAway
```

4. **Initialize the Client**: Initialize the `OneBusAway` client with the desired base URL (default is `api.pugetsound.onebusaway.org`):

```python
oba = OneBusAway(base_url="api.pugetsound.onebusaway.org")
```

5. **Use the Client**: Now you can start using the client to interact with the OneBusAway API:

```python
# Get a list of agencies with coverage
agencies = oba.agency_with_coverage()

# Get arrivals and departures for a stop
stop_id = "1_75403"
arrivals_and_departures = oba.arrivals_and_departures_for_stop(stop_id)
```

For more examples and detailed usage instructions, please refer to the [Usage](#usage) section.

## Usage

The OneBusAway Python Client provides a wide range of methods to interact with the OneBusAway API. Here are some examples:

### Agencies

```python
# Get a list of agencies with coverage
agencies = oba.agency_with_coverage()

# Get details for a specific agency
agency_details = oba.agency("1", get_references=True)
```

### Stops

```python
# Get arrivals and departures for a stop
stop_id = "1_75403"
arrivals_and_departures = oba.arrivals_and_departures_for_stop(stop_id)

# Get schedule for a stop
stop_schedule = oba.schedule_for_stop(stop_id)
```

### Routes

```python
# Get routes for an agency
agency_id = "1"
routes = oba.routes_for_agency(agency_id)

# Get schedule for a route
route_id = "1_100"
route_schedule = oba.schedule_for_route(route_id)
```

### Trips

```python
# Get trips for a route
route_id = "1_100"
trips = oba.trips_for_route(route_id, includeSchedule=True)

# Get trip details
trip_id = "1_12345"
trip_details = oba.trip_details(trip_id, includeSchedule=True)
```

### Vehicles

```python
# Get vehicles for an agency
agency_id = "1"
vehicles = oba.vehicles_for_agency(agency_id)
```

For more details and a complete list of available methods, please refer to the [API Reference](#api-reference) section.

## API Reference

The OneBusAway Python Client provides the following methods:

### `OneBusAway` Class

- `agency_with_coverage(get_references: bool = False) -> List[Agency]`
- `agency(id: str, get_references: bool = False) -> AgencyDetails`
- `arrival_and_departure_for_stop(id: str, tripId: str, serviceDate: int, vehicleId: Optional[str] = None, stopSequence: Optional[int] = None, get_references: bool = False) -> ArrivalAndDeparture`
- `arrivals_and_departures_for_stop(id: str, minutesBefore: Optional[int] = None, minutesAfter: Optional[int] = None, get_references: bool = False) -> StopWithArrivalsAndDepartures`
- `block(id: str, get_references: bool = False) -> Block`
- `get_config(get_references: bool = False) -> Dict[str, Any]`
- `current_time(get_references: bool = False) -> datetime`
- `report_problem_with_stop(stopId: str, code: str, userComment: Optional[str] = None, userLat: Optional[float] = None, userLon: Optional[float] = None, userLocationAccuracy: Optional[float] = None) -> bool`
- `report_problem_with_trip(tripId: str, serviceDate: int, vehicleId: str, stopId: str, code: str, userComment: Optional[str] = None, userOnVehicle: Optional[bool] = None, userVehicleNumber: Optional[str] = None, userLat: Optional[float] = None, userLon: Optional[float] = None, userLocationAccuracy: Optional[float] = None) -> None`
- `route_ids_for_agency(id: str, get_references: bool = False) -> List[str]`
- `route(id: str, get_references: bool = False) -> Route`
- `routes_for_agency(id: str, get_references: bool = False) -> List[Route]`
- `routes_for_location(lat: float, lon: float, radius: Optional[int] = None, latSpan: Optional[float] = None, lonSpan: Optional[float] = None, query: Optional[str] = None, get_references: bool = False) -> List[Route]`
- `schedule_for_route(id: str, date: Optional[str] = None, get_references: bool = False) -> RouteSchedule`
- `schedule_for_stop(id: str, date: Optional[str] = None, get_references: bool = False) -> StopSchedule`
- `shape(id: str, get_references: bool = False) -> EncodedPolyline`
- `stop_ids_for_agency(id: str, get_references: bool = False) -> List[str]`
- `stop(id: str, get_references: bool = False) -> Stop`
- `stops_for_location(lat: float, lon: float, radius: Optional[int] = None, latSpan: Optional[float] = None, lonSpan: Optional[float] = None, query: Optional[str] = None, get_references: bool = False) -> List[Stop]`
- `stops_for_route(id: str, includePolylines: Optional[bool] = None, time: Optional[str] = None, get_references: bool = False) -> StopsForRoute`
- `trip_details(id: str, serviceDate: Optional[int] = None, includeTrip: Optional[bool] = None, includeSchedule: Optional[bool] = None, includeStatus: Optional[bool] = None, time: Optional[str] = None, get_references: bool = False) -> TripDetails`
- `trip_for_vehicle(id: str, includeTrip: Optional[bool] = None, includeSchedule: Optional[bool] = None, includeStatus: Optional[bool] = None, time: Optional[str] = None, get_references: bool = False) -> TripDetails`
- `trip(id: str, get_references: bool = False) -> Trip`
- `trips_for_location(lat: float, lon: float, latSpan: float, lonSpan: float, includeTrip: Optional[bool] = None, includeSchedule: Optional[bool] = None, time: Optional[str] = None, get_references: bool = False) -> List[TripDetails]`
- `trips_for_route(id: str, includeStatus: Optional[bool] = None, includeSchedule: Optional[bool] = None, time: Optional[str] = None, get_references: bool = False) -> List[TripDetails]`
- `vehicles_for_agency(id: str, time: Optional[str] = None, get_references: bool = False) -> List[VehicleStatus]`

For detailed information on each method, including parameter descriptions and return types, please refer to the [API Documentation](https://onebusaway.readthedocs.io/en/latest/api.html).

## Contributing

We welcome and appreciate contributions from the community! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/cheeksthegeek/onebusaway-python).

To contribute, follow these steps:

1. **Fork the repository** on GitHub.
2. **Create a new branch** for your feature or bug fix: `git checkout -b my-new-feature`.
3. **Make your changes** and commit them: `git commit -am 'Add some feature'`.
4. **Push your changes** to your forked repository: `git push origin my-new-feature`.
5. **Create a new pull request** on the main repository.

Please ensure that your code adheres to the project's coding standards and that all tests pass before submitting a pull request.

## License

The OneBusAway Python Client is released under the [MIT License](https://opensource.org/licenses/MIT).

## Support

If you have any questions, or issues, or need further assistance, please open an issue on the [GitHub repository](https://github.com/cheeksthegeek/onebusaway-python) or join our [discussion forum](https://github.com/cheeksthegeek/onebusaway-python/discussions).

## Acknowledgments

The OneBusAway Python Client was inspired by the [OneBusAway API](https://onebusaway.org/) and the need for a robust and easy-to-use Python library to interact with it. We would like to express our gratitude to the OneBusAway team and the open-source community for their contributions and support.