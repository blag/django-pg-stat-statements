#!/bin/bash

while ! pg_isready; do
	echo "Waiting for PostgreSQL to start up"
	sleep 1
done

exec $@
