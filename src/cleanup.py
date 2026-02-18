import os
import time

def delete_old_reports(days=14):
    folder_path = "reports"
    if not os.path.exists(folder_path):
        return

    # Convert days to seconds
    seconds = days * 24 * 60 * 60
    current_time = time.time()

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # Check if it's a file and if it's older than our threshold
        if os.path.isfile(file_path):
            file_age = os.path.getmtime(file_path)
            if current_time - file_age > seconds:
                print(f"🗑️ Deleting old report: {filename}")
                os.remove(file_path)

if __name__ == "__main__":
    delete_old_reports()