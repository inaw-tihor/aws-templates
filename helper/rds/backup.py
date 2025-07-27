import boto3
from datetime import datetime

rds = boto3.client('rds')
snapshot_id = "manual-snap-" + datetime.now().strftime('%Y%m%d%H%M%S')

rds.create_db_snapshot(
    DBInstanceIdentifier="rds-postgres-minimal-rdsinstance-mxdcpdxhiu5l",
    DBSnapshotIdentifier=snapshot_id
)
