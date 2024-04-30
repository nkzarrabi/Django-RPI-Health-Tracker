import math
import requests
import json


api_url = 'https://squid-app-jppji.ondigitalocean.app/graphql/'

def calculate_change(current, previous):
    return abs(current - previous)

def analyze_movement(data_points, change_threshold, consecutive_threshold):
    significant_movements = 0
    previous = data_points[0]
    
    for current in data_points[1:]:
        change_x = calculate_change(current['x'], previous['x'])
        change_y = calculate_change(current['y'], previous['y'])
        change_z = calculate_change(current['z'], previous['z'])
        
        if change_x > change_threshold or change_y > change_threshold or change_z > change_threshold:
            significant_movements += 1
            if significant_movements >= consecutive_threshold:
                return True  # Indicates consistent significant movement
        else:
            significant_movements = 0  # Reset if the movement drops below threshold
        
        previous = current
    
    return False


def prepare_data_for_api(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data_points = []
    for line in lines:
        parts = line.strip().split(',')
        timestamp, x, y, z = parts[0], int(parts[1]), int(parts[2]), int(parts[3])
        data_points.append({'timestamp': timestamp, 'x': x, 'y': y, 'z': z})

    total_change_x = 0
    total_change_y = 0
    total_change_z = 0

    for i in range(1, len(data_points)):
        total_change_x += calculate_change(data_points[i]['x'], data_points[i-1]['x'])
        total_change_y += calculate_change(data_points[i]['y'], data_points[i-1]['y'])
        total_change_z += calculate_change(data_points[i]['z'], data_points[i-1]['z'])

    average_change_x = round(total_change_x / (len(data_points) - 1))
    average_change_y = round(total_change_y / (len(data_points) - 1))
    average_change_z = round(total_change_z / (len(data_points) - 1))

    intensity = f'delta_x{average_change_x}, delta_y{average_change_y} + delta_z{average_change_z}'
    if analyze_movement(data_points, change_threshold=50, consecutive_threshold=5):
        # Prepare and return data for API if sleepwalking is detected
        start_time = data_points[0]['timestamp']
        end_time = data_points[-1]['timestamp']
        return {'startTime': start_time, 'endTime': end_time, 'intensity': 'Movements-'+ intensity}
    
    return None  # No significant sleepwalking detected

def send_data_to_server(data):
    url = api_url  # Ensure this is the correct address
    headers = {'Content-Type': 'application/json'}
    
    query = """
    mutation CreateSleepwalkingEvent($startTime: DateTime!, $endTime: DateTime!, $intensity: String!) {
        createSleepwalkingEvent(startTime: $startTime, endTime: $endTime, intensity: $intensity) {
            sleepwalkingEvent {
                id
                startTime
                endTime
                intensity
            }
        }
    }
    """
    response = requests.post(url, json={'query': query, 'variables': data}, headers=headers)
    print(response.text)

# Example usage
data = prepare_data_for_api("data_scripts/microbit_data.txt")
if data:
    print(data)
    send_data_to_server(data)
