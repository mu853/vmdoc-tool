#!/bin/bash
sqlite3 summary.db << EOS
drop table if exists nsx;
.mode csv
.import summary.csv nsx
EOS
