import boto3
import time

# Replace these values
snapshot_identifier = 'manual-snap-20250727193453'  # your snapshot name
restored_db_instance_identifier = 'restored-postgres-db'
db_instance_class = 'db.t3.micro'
subnet_group = 'rds-postgres-minimal-rdssubnetgroup-oflw3loljjco'  # e.g., 'rds-postgres-minimal-rdssubnetgroup-xyz'
security_group_id = 'sg-0e094088610e3644b'  # must allow PostgreSQL (port 5432)
region = 'us-east-1'

rds = boto3.client('rds', region_name=region)

try:
    print(f"Restoring DB from snapshot: {snapshot_identifier}...")
    response = rds.restore_db_instance_from_db_snapshot(
        DBInstanceIdentifier=restored_db_instance_identifier,
        DBSnapshotIdentifier=snapshot_identifier,
        DBInstanceClass=db_instance_class,
        PubliclyAccessible=True,
        DBSubnetGroupName=subnet_group,
        VpcSecurityGroupIds=[security_group_id],
        Tags=[
            {'Key': 'Name', 'Value': 'RestoredPostgres'}
        ]
    )
    print("Restore request submitted successfully.")
except Exception as e:
    print(f"Error restoring DB: {e}")
    exit(1)

# Optional: Wait for DB to become available
print("Waiting for the DB to become available...")
waiter = rds.get_waiter('db_instance_available')
waiter.wait(DBInstanceIdentifier=restored_db_instance_identifier)

# Print endpoint
restored_info = rds.describe_db_instances(DBInstanceIdentifier=restored_db_instance_identifier)
endpoint = restored_info['DBInstances'][0]['Endpoint']['Address']
print(f"✅ Restored DB Endpoint: {endpoint}")
