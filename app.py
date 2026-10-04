import json
import platform

def get_system_summary():
    return {
        "status": "HEALTHY",
        "os": platform.system(),
        "release": platform.release()
    }

if __name__ == '__main__':
    print(json.dumps(get_system_summary(), indent=2))
