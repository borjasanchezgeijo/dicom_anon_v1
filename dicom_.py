import os
import pydicom

def anonymize_dicom_folder(folder_path):
    count = 0  

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.dcm'):
            file_path = os.path.join(folder_path, filename)
            ds = pydicom.dcmread(file_path)

            print(f"Before anonymization: {filename}")
            print("PatientName:", ds.get("PatientName", "NOT PRESENT"))
            print("PatientID:", ds.get("PatientID", "NOT PRESENT"))
            print("ReferringPhysicianName:", ds.get("ReferringPhysicianName", "NOT PRESENT"))
            print("-" * 40)

            # Anonymize
            if 'PatientName' in ds: ds.PatientName = 'anon'
            if 'PatientID' in ds: ds.PatientID = '0000'
            if 'ReferringPhysicianName' in ds: ds.ReferringPhysicianName = 'anon'
            if 'InstitutionName' in ds: ds.InstitutionName = 'anon'

            # Overwrite
            ds.save_as(file_path)
            count += 1  # ← increment after successful save

            # Reload and check
            ds_check = pydicom.dcmread(file_path)
            print(f"After anonymization: {filename}")
            print("PatientName:", ds_check.get("PatientName", "NOT PRESENT"))
            print("PatientID:", ds_check.get("PatientID", "NOT PRESENT"))
            print("ReferringPhysicianName:", ds_check.get("ReferringPhysicianName", "NOT PRESENT"))
            print("=" * 40)

    print(f"anon'd count: {count}")

# Function call
anonymize_dicom_folder("/Users/borjasanchez/Desktop/DICOM")
