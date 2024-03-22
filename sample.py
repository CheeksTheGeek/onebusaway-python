# sample.py
import os
from onebusaway import OneBusAway, OneBusAwayException

# Set your API key

# Initialize the client
oba = OneBusAway(base_url="api.pugetsound.onebusaway.org")

try:
    # Get a list of agencies with coverage
    agencies = oba.agency_with_coverage()
    print("Agencies with coverage:")
    for agency in agencies:
        print(f"({agency.agencyId}) {agency.lat}, {agency.lon}")

    # Get details for a specific agency
    agency_details = oba.agency("1", get_references=True)
    print(f"\nAgency Details for {agency_details.name}:")
    print(agency_details)

    # Get arrivals and departures for a stop
    stop_id = "1_75403"
    arrivals_and_departures = oba.arrivals_and_departures_for_stop(stop_id)
    print(f"\nArrivals and Departures for Stop {stop_id}:")
    for arrival_departure in arrivals_and_departures.arrivalsAndDepartures:
        print(arrival_departure)

    # Get a block
    block_id = "1_7087406"
    block = oba.block(block_id, get_references=True)
    print(f"\nBlock {block_id}:")
    print(block)

    # Get routes for an agency
    agency_id = "1"
    routes = oba.routes_for_agency(agency_id)
    print(f"\nRoutes for Agency {agency_id}:")
    for route in routes:
        print(f"- {route.shortName} ({route.id})")

    # Get stop schedule
    stop_id = "1_75403"
    stop_schedule = oba.schedule_for_stop(stop_id)
    print(f"\nSchedule for Stop {stop_id}:")
    print(stop_schedule)

    # Get trips for a route
    route_id = "1_100"
    trips = oba.trips_for_route(route_id, includeSchedule=True)
    print(f"\nTrips for Route {route_id}:")
    for trip in trips:
        print(trip)

    # Get vehicles for an agency
    agency_id = "1"
    vehicles = oba.vehicles_for_agency(agency_id)
    print(f"\nVehicles for Agency {agency_id}:")
    for vehicle in vehicles:
        print(vehicle)

except OneBusAwayException as e:
    print(f"Error: {e}")
