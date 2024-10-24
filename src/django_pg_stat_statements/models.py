from django.conf import settings
from django.db import models


class QueryStatistic(models.Model):
    dbid = models.BigIntegerField(help_text="OID of database in which the statement was executed")
    userid = models.BigIntegerField(help_text="OID of user who executed the statement")
    queryid = models.BigIntegerField(primary_key=True, help_text="Internal hash code, computed from the statement's parse tree")
    query = models.TextField(help_text="Text of a representative statement")
    rows = models.BigIntegerField(help_text="Total number of rows retrieved or affected by the statement")
    calls = models.BigIntegerField(help_text="Number of times executed")

    total_exec_time = models.FloatField(help_text="Total time spent executing the statement, in milliseconds")
    min_exec_time = models.FloatField(help_text="Minimum time spent executing the statement, in milliseconds")
    max_exec_time = models.FloatField(help_text="Maximum time spent executing the statement, in milliseconds")
    mean_exec_time = models.FloatField(help_text="Mean time spent executing the statement, in milliseconds")
    stddev_exec_time = models.FloatField(help_text="Population standard deviation of time spent executing the statement, in milliseconds")

    plans = models.BigIntegerField(help_text="Number of times the statement was planned (if pg_stat_statements.track_planning is enabled, otherwise zero)")
    total_plan_time = models.BigIntegerField(help_text="Total time spent planning the statement, in milliseconds (if pg_stat_statements.track_planning is enabled, otherwise zero)")
    min_plan_time = models.BigIntegerField(help_text="Minimum time spent planning the statement, in milliseconds (if pg_stat_statements.track_planning is enabled, otherwise zero)")
    max_plan_time = models.BigIntegerField(help_text="Maximum time spent planning the statement, in milliseconds (if pg_stat_statements.track_planning is enabled, otherwise zero)")
    mean_plan_time = models.BigIntegerField(help_text="Mean time spent planning the statement, in milliseconds (if pg_stat_statements.track_planning is enabled, otherwise zero)")
    stddev_plan_time = models.BigIntegerField(help_text="Population standard deviation of time spent planning the statement, in milliseconds (if pg_stat_statements.track_planning is enabled, otherwise zero)")

    shared_blks_hit = models.BigIntegerField(help_text="Total number of shared block cache hits by the statement")
    shared_blks_read = models.BigIntegerField(help_text="Total number of shared blocks read by the statement")
    shared_blks_dirtied = models.BigIntegerField(help_text="Total number of shared blocks dirtied by the statement")
    shared_blks_written = models.BigIntegerField(help_text="Total number of shared blocks written by the statement")
    if settings.POSTGRES_VERSION >= (17,):
        shared_blk_read_time = models.FloatField(help_text="Total time the statement spent reading shared blocks, in milliseconds (if track_io_timing is enabled, otherwise zero)")
        shared_blk_write_time = models.FloatField(help_text="Total time the statement spent writing shared blocks, in milliseconds (if track_io_timing is enabled, otherwise zero)")

    shared_blks_hit = models.BigIntegerField(help_text="Total number of local block cache hits by the statement")
    local_blks_read = models.BigIntegerField(help_text="Total number of local blocks read by the statement")
    local_blks_dirtied = models.BigIntegerField(help_text="Total number of local blocks dirtied by the statement")
    local_blks_written = models.BigIntegerField(help_text="Total number of local blocks written by the statement")
    if settings.POSTGRES_VERSION >= (17,):
        local_blk_read_time = models.FloatField(help_text="Total time the statement spent reading local blocks, in milliseconds (if track_io_timing is enabled, otherwise zero)")
        local_blk_write_time = models.FloatField(help_text="Total time the statement spent writing local blocks, in milliseconds (if track_io_timing is enabled, otherwise zero)")

    temp_blks_read = models.BigIntegerField(help_text="Total number of temp blocks read by the statement")
    temp_blks_written = models.BigIntegerField(help_text="Total number of temp blocks written by the statement")
    if settings.POSTGRES_VERSION < (17,):
        blk_read_time = models.FloatField(help_text="Total time the statement spent reading data file blocks, in milliseconds (if track_io_timing is enabled, otherwise zero)")
        blk_write_time = models.FloatField(help_text="Total time the statement spent writing data file blocks, in milliseconds (if track_io_timing is enabled, otherwise zero)")
    if settings.POSTGRES_VERSION >= (15,):
        temp_blk_read_time = models.FloatField(help_text="Total time the statement spent reading temp file blocks, in milliseconds (if track_io_timing is enabled, otherwise zero)")
        temp_blk_write_time = models.FloatField(help_text="Total time the statement spent writing temp file blocks, in milliseconds (if track_io_timing is enabled, otherwise zero)")

    wal_records = models.BigIntegerField(help_text="Total number of WAL records generated by the statement")
    wal_fpi = models.BigIntegerField(help_text="Total number of WAL full page images generated by the statement")
    wal_bytes = models.DecimalField(max_digits=20, decimal_places=2, help_text="Total amount of WAL generated by the statement in bytes")

    class Meta:
        managed = False
        db_table = "pg_stat_statements"
        ordering = ("-mean_exec_time",)
        verbose_name = "Query Statistic"
        verbose_name_plural = "Query Statistics"
