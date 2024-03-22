import os
import time
from genson import SchemaBuilder
import json
from onebusaway.client_json import OneBusAwayJSON


def generate_schema(json_data):
    builder = SchemaBuilder()
    builder.add_object(json_data)
    schema = builder.to_schema()
    if "required" in schema:
        del schema["required"]

    def remove_required_keys(d):
        if isinstance(d, dict):
            return {k: remove_required_keys(v) for k, v in d.items() if k != "required"}
        elif isinstance(d, list):
            return [remove_required_keys(v) for v in d]
        else:
            return d

    schema = remove_required_keys(schema)
    return schema


schema_dir = "schemas/ps"
if not os.path.exists(schema_dir):
    os.makedirs(schema_dir)
oba = OneBusAwayJSON(base_url="api.pugetsound.onebusaway.org", api_key="TEST")
# PUGET SOUND
methods = [
    (oba.agency_with_coverage,),  # oba.agency_with_coverage()
    (oba.agency, "1"),  # oba.agency("1")
    (
        oba.arrival_and_departure_for_stop,
        "1_5810",
        "1_475802825",
        1710745200000,
    ),  # oba.arrival_and_departure_for_stop("1_5810", "1_475802825", 1710745200000)
    (
        oba.arrivals_and_departures_for_stop,
        "1_5810",
        5,
        5,
    ),  # oba.arrivals_and_departures_for_stop("1_5810", 5, 5)
    (oba.block, "1_7087406"),  # oba.block("1_7087406")
    (oba.get_config,),  # oba.get_config()
    (oba.current_time,),  # oba.current_time()
    (
        oba.report_problem_with_stop,
        "1_7430",
        "other",
    ),  # oba.report_problem_with_stop("1_7430", "other")
    (
        oba.report_problem_with_trip,
        "1_79430293",
        1291536000000,
        "1_3521",
        "1_75403",
        "vehicle_never_came",
    ),  # oba.report_problem_with_trip("1_79430293", 1291536000000, "1_3521", "1_75403", "vehicle_never_came")
    (oba.route_ids_for_agency, "1"),  # oba.route_ids_for_agency("1")
    (oba.route, "1_100264"),  # oba.route("1_100264")
    (oba.routes_for_agency, "1"),  # oba.routes_for_agency("1")
    (
        oba.routes_for_location,
        47.653435,
        -122.305641,
    ),  # oba.routes_for_location(47.653435, -122.305641)
    (oba.schedule_for_route, "1_100264"),  # oba.schedule_for_route("1_100264")
    (oba.schedule_for_stop, "1_75403"),  # oba.schedule_for_stop("1_75403")
    (oba.shape, "1_10002005"),  # oba.shape("1_10002005")
    (oba.stop_ids_for_agency, 1),  # oba.stop_ids_for_agency(1)
    (oba.stop, "1_75403"),  # oba.stop("1_75403")
    (
        oba.stops_for_location,
        47.653435,
        -122.305641,
    ),  # oba.stops_for_location(47.653435, -122.305641)
    (oba.stops_for_route, "1_100264"),  # oba.stops_for_route("1_100264")
    (oba.trip_details, "1_475802825"),  # oba.trip_details("1_475802825")
    (oba.trip_for_vehicle, "1_6956"),  # oba.trip_for_vehicle("1_6956")
    (oba.trip, "1_571643895"),  # oba.trip("1_571643895")
    (
        oba.trips_for_location,
        47.6097,
        122.3331,
        0.01,
        0.01,
    ),  # oba.trips_for_location(47.6097, 122.3331, 0.01, 0.01)
    (oba.trips_for_route, "1_100264"),  # oba.trips_for_route("1_100264")
    (oba.vehicles_for_agency, 1),  # oba.vehicles_for_agency(1)
]


# MTA
# methods = [
#     (oba.agency_with_coverage,),
#     (oba.agency, "MTA NYCT"),
#     (oba.arrival_and_departure_for_stop, "1_75403", "1_15551325", 1609459200000),
#     (oba.arrivals_and_departures_for_stop, "1_75403", 5, 5),
#     (oba.block, "1_100264"),
#     # (oba.get_config,),
#     (oba.current_time_unix_epoch,),
#     (oba.current_time,),
#     # (oba_mta.report_problem_with_stop, "1_901704", "stop_closed"),
#     # (
#     #     oba_mta.report_problem_with_trip,
#     #     "1_15551325",
#     #     1609459200000,
#     #     "1_3526",
#     #     "1_75403",
#     #     "late",
#     # ),
#     (oba.route_ids_for_agency, "MTA NYCT"),
#     (oba.route, "B63"),
#     (oba.routes_for_agency, "MTA NYCT"),
#     (oba.routes_for_location, 47.6097, 122.3331),
#     (oba.schedule_for_route, "1_100264"),
#     (oba.schedule_for_stop, "1_75403"),
#     (oba.shape, "1_100264"),
#     (oba.stop_ids_for_agency, 1),
#     (oba.stop, "1_75403"),
#     (oba.stops_for_location, 47.6097, 122.3331),
#     (oba.stops_for_route, "1_100264"),
#     (oba.trip_details, "1_15551325"),
#     (oba.trip_for_vehicle, "1_3526"),
#     (oba.trip, "1_15551325"),
#     (oba.trips_for_location, 47.6097, 122.3331, 0.01, 0.01),
#     (oba.trips_for_route, "1_100264"),
#     (oba.vehicles_for_agency, 1),
# ]
def gen_schema_for_methods():
    for i, (method, *args) in enumerate(methods):
        method_name = method.__name__
        while True:
            response = method(*args)
            if response.status_code == 200:
                break
            if response.status_code == 400 or response.status_code == 404:
                print(f"Error: {response.status_code}. Skipping method_{method_name}")
                break
            print(
                f"Error {response.status_code} in running {method_name}. Retrying in 5 seconds..."
            )
            time.sleep(5)
        try:
            json_data = response.json()
        except json.decoder.JSONDecodeError:
            print(
                f"Failed to decode JSON for method_{method_name}. Response content: {response.text}"
            )
            break
        schema = generate_schema(json_data)
        with open(f"{schema_dir}/{method_name}.json", "w") as file:
            json.dump(schema, file, indent=4)
        print(
            f"Schema for {method_name} has been generated and saved to {schema_dir}/{method_name}.json"
        )
        time.sleep(1)


gen_schema_for_methods()
