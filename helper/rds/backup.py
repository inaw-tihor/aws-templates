import boto3
from datetime import datetime

rds = boto3.client('rds')
snapshot_id = "manual-snap-" + datetime.now().strftime('%Y%m%d%H%M%S')
db_instance_identifier="rds-postgres-minimal-rdsinstance-mxdcpdxhiu5l"

rds.create_db_snapshot(
    DBInstanceIdentifier=db_instance_identifier,
    DBSnapshotIdentifier=snapshot_id
)
