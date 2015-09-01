# -*- coding: utf-8; -*-

#-----------------------------------------------------------------------------
# This module contains rrdgraph definitions for collecd plugins. The following
# naming convention is used to keep things simple and flat:
#
#   1. Variables starting with 'graph_$name' ...
#   2. Variables starting with 'stacked_graph_$name'
#

graph_apache_bytes = r'''
DEF:min_raw={file}:value:MIN
DEF:avg_raw={file}:value:AVERAGE
DEF:max_raw={file}:value:MAX
CDEF:min=min_raw8*
CDEF:avg=avg_raw8*
CDEF:max=max_raw8*
CDEF:mytime=avg_rawTIMETIMEIF
CDEF:sample_len_raw=mytimePREV(mytime)-
CDEF:sample_len=sample_len_rawUN0sample_len_rawIF
CDEF:avg_sample=avg_rawUN0avg_rawIFsample_len*
CDEF:avg_sum=PREVUN0PREVIFavg_sample+
AREA:avg#{colors[HalfBlue]}
LINE1:avg#{colors[FullBlue]}:Bit/s
GPRINT:min:MIN:%5.1lf%s Min
GPRINT:avg:AVERAGE:%5.1lf%s Avg
GPRINT:max:MAX:%5.1lf%s Max
GPRINT:avg:LAST:%5.1lf%s Last
GPRINT:avg_sum:LAST:(ca. %5.1lf%sB Total)\l
'''

graph_apache_connections = r'''
DEF:min={file}:value:MIN
DEF:avg={file}:value:AVERAGE
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Connections
GPRINT:min:MIN:%6.2lf Min
GPRINT:avg:AVERAGE:%6.2lf Avg
GPRINT:max:MAX:%6.2lf Max
GPRINT:avg:LAST:%6.2lf Last
'''

graph_apache_idle_workers = r'''
DEF:min={file}:value:MIN
DEF:avg={file}:value:AVERAGE
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Idle Workers
GPRINT:min:MIN:%6.2lf Min
GPRINT:avg:AVERAGE:%6.2lf Avg
GPRINT:max:MAX:%6.2lf Max
GPRINT:avg:LAST:%6.2lf Last
'''

graph_apache_requests = r'''
DEF:min={file}:value:MIN
DEF:avg={file}:value:AVERAGE
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Requests/s
GPRINT:min:MIN:%6.2lf Min
GPRINT:avg:AVERAGE:%6.2lf Avg
GPRINT:max:MAX:%6.2lf Max
GPRINT:avg:LAST:%6.2lf Last
'''

graph_apache_scoreboard = r'''
DEF:min={file}:value:MIN
DEF:avg={file}:value:AVERAGE
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Processes
GPRINT:min:MIN:%6.2lf Min
GPRINT:avg:AVERAGE:%6.2lf Avg
GPRINT:max:MAX:%6.2lf Max
GPRINT:avg:LAST:%6.2lf Last
'''

graph_bitrate = r'''
-v
Bits/s
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Bits/s
GPRINT:min:MIN:%5.1lf%s Min
GPRINT:avg:AVERAGE:%5.1lf%s Average
GPRINT:max:MAX:%5.1lf%s Max
GPRINT:avg:LAST:%5.1lf%s Last\l
'''

graph_charge = r'''
-v
Ah
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Charge
GPRINT:min:MIN:%5.1lf%sAh Min
GPRINT:avg:AVERAGE:%5.1lf%sAh Avg
GPRINT:max:MAX:%5.1lf%sAh Max
GPRINT:avg:LAST:%5.1lf%sAh Last\l
'''

graph_connections = r'''
-v
Connections
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Connections
GPRINT:min:MIN:%4.1lf Min
GPRINT:avg:AVERAGE:%4.1lf Avg
GPRINT:max:MAX:%4.1lf Max
GPRINT:avg:LAST:%4.1lf Last\l
'''

graph_cpu = r'''
-v
CPU load
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Percent
GPRINT:min:MIN:%6.2lf%% Min
GPRINT:avg:AVERAGE:%6.2lf%% Avg
GPRINT:max:MAX:%6.2lf%% Max
GPRINT:avg:LAST:%6.2lf%% Last\l
'''

graph_current = r'''
-v
Ampere
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Current
GPRINT:min:MIN:%5.1lf%sA Min
GPRINT:avg:AVERAGE:%5.1lf%sA Avg
GPRINT:max:MAX:%5.1lf%sA Max
GPRINT:avg:LAST:%5.1lf%sA Last\l
'''

graph_df = r'''
-v
Percent
-l
0
DEF:free_avg={file}:free:AVERAGE
DEF:free_min={file}:free:MIN
DEF:free_max={file}:free:MAX
DEF:used_avg={file}:used:AVERAGE
DEF:used_min={file}:used:MIN
DEF:used_max={file}:used:MAX
CDEF:total=free_avgused_avg+
CDEF:free_pct=100free_avg*total/
CDEF:used_pct=100used_avg*total/
CDEF:free_acc=free_pctused_pct+
CDEF:used_acc=used_pct
AREA:free_acc#{colors[HalfGreen]}
AREA:used_acc#{colors[HalfRed]}
LINE1:free_acc#{colors[FullGreen]}:Free
GPRINT:free_min:MIN:%5.1lf%sB Min
GPRINT:free_avg:AVERAGE:%5.1lf%sB Avg
GPRINT:free_max:MAX:%5.1lf%sB Max
GPRINT:free_avg:LAST:%5.1lf%sB Last\l
LINE1:used_acc#{colors[FullRed]}:Used
GPRINT:used_min:MIN:%5.1lf%sB Min
GPRINT:used_avg:AVERAGE:%5.1lf%sB Avg
GPRINT:used_max:MAX:%5.1lf%sB Max
GPRINT:used_avg:LAST:%5.1lf%sB Last\l
'''

graph_disk = r'''
DEF:rtime_avg={file}:rtime:AVERAGE
DEF:rtime_min={file}:rtime:MIN
DEF:rtime_max={file}:rtime:MAX
DEF:wtime_avg={file}:wtime:AVERAGE
DEF:wtime_min={file}:wtime:MIN
DEF:wtime_max={file}:wtime:MAX
CDEF:rtime_avg_ms=rtime_avg1000/
CDEF:rtime_min_ms=rtime_min1000/
CDEF:rtime_max_ms=rtime_max1000/
CDEF:wtime_avg_ms=wtime_avg1000/
CDEF:wtime_min_ms=wtime_min1000/
CDEF:wtime_max_ms=wtime_max1000/
CDEF:total_avg_ms=rtime_avg_mswtime_avg_ms+
CDEF:total_min_ms=rtime_min_mswtime_min_ms+
CDEF:total_max_ms=rtime_max_mswtime_max_ms+
AREA:total_max_ms#{colors[HalfRed]}
AREA:total_min_ms#{colors[Canvas]}
LINE1:wtime_avg_ms#{colors[FullGreen]}:Write
GPRINT:wtime_min_ms:MIN:%5.1lf%s Min
GPRINT:wtime_avg_ms:AVERAGE:%5.1lf%s Avg
GPRINT:wtime_max_ms:MAX:%5.1lf%s Max
GPRINT:wtime_avg_ms:LAST:%5.1lf%s Last\n
LINE1:rtime_avg_ms#{colors[FullBlue]}:Read
GPRINT:rtime_min_ms:MIN:%5.1lf%s Min
GPRINT:rtime_avg_ms:AVERAGE:%5.1lf%s Avg
GPRINT:rtime_max_ms:MAX:%5.1lf%s Max
GPRINT:rtime_avg_ms:LAST:%5.1lf%s Last\n
LINE1:total_avg_ms#{colors[FullRed]}:Total
GPRINT:total_min_ms:MIN:%5.1lf%s Min
GPRINT:total_avg_ms:AVERAGE:%5.1lf%s Avg
GPRINT:total_max_ms:MAX:%5.1lf%s Max
GPRINT:total_avg_ms:LAST:%5.1lf%s Last
'''

graph_disk_octets = r'''
-v
Bytes/s
DEF:out_min={file}:write:MIN
DEF:out_avg={file}:write:AVERAGE
DEF:out_max={file}:write:MAX
DEF:inc_min={file}:read:MIN
DEF:inc_avg={file}:read:AVERAGE
DEF:inc_max={file}:read:MAX
CDEF:overlap=out_avginc_avgGTinc_avgout_avgIF
CDEF:mytime=out_avgTIMETIMEIF
CDEF:sample_len_raw=mytimePREV(mytime)-
CDEF:sample_len=sample_len_rawUN0sample_len_rawIF
CDEF:out_avg_sample=out_avgUN0out_avgIFsample_len*
CDEF:out_avg_sum=PREVUN0PREVIFout_avg_sample+
CDEF:inc_avg_sample=inc_avgUN0inc_avgIFsample_len*
CDEF:inc_avg_sum=PREVUN0PREVIFinc_avg_sample+
AREA:out_avg#{colors[HalfGreen]}
AREA:inc_avg#{colors[HalfBlue]}
AREA:overlap#{colors[HalfBlueGreen]}
LINE1:out_avg#{colors[FullGreen]}:Written
GPRINT:out_avg:AVERAGE:%5.1lf%s Avg
GPRINT:out_max:MAX:%5.1lf%s Max
GPRINT:out_avg:LAST:%5.1lf%s Last
GPRINT:out_avg_sum:LAST:(ca. %5.1lf%sB Total)\l
LINE1:inc_avg#{colors[FullBlue]}:Read
GPRINT:inc_avg:AVERAGE:%5.1lf%s Avg
GPRINT:inc_max:MAX:%5.1lf%s Max
GPRINT:inc_avg:LAST:%5.1lf%s Last
GPRINT:inc_avg_sum:LAST:(ca. %5.1lf%sB Total)\l
'''

graph_disk_merged = r'''
-v
Merged Ops/s
DEF:out_min={file}:write:MIN
DEF:out_avg={file}:write:AVERAGE
DEF:out_max={file}:write:MAX
DEF:inc_min={file}:read:MIN
DEF:inc_avg={file}:read:AVERAGE
DEF:inc_max={file}:read:MAX
CDEF:overlap=out_avginc_avgGTinc_avgout_avgIF
AREA:out_avg#{colors[HalfGreen]}
AREA:inc_avg#{colors[HalfBlue]}
AREA:overlap#{colors[HalfBlueGreen]}
LINE1:out_avg#{colors[FullGreen]}:Written
GPRINT:out_avg:AVERAGE:%6.2lf Avg
GPRINT:out_max:MAX:%6.2lf Max
GPRINT:out_avg:LAST:%6.2lf Last\l
LINE1:inc_avg#{colors[FullBlue]}:Read
GPRINT:inc_avg:AVERAGE:%6.2lf Avg
GPRINT:inc_max:MAX:%6.2lf Max
GPRINT:inc_avg:LAST:%6.2lf Last\l
'''

graph_disk_ops = r'''
-v
Ops/s
DEF:out_min={file}:write:MIN
DEF:out_avg={file}:write:AVERAGE
DEF:out_max={file}:write:MAX
DEF:inc_min={file}:read:MIN
DEF:inc_avg={file}:read:AVERAGE
DEF:inc_max={file}:read:MAX
CDEF:overlap=out_avginc_avgGTinc_avgout_avgIF
AREA:out_avg#{colors[HalfGreen]}
AREA:inc_avg#{colors[HalfBlue]}
AREA:overlap#{colors[HalfBlueGreen]}
LINE1:out_avg#{colors[FullGreen]}:Written
GPRINT:out_avg:AVERAGE:%6.2lf Avg
GPRINT:out_max:MAX:%6.2lf Max
GPRINT:out_avg:LAST:%6.2lf Last\l
LINE1:inc_avg#{colors[FullBlue]}:Read
GPRINT:inc_avg:AVERAGE:%6.2lf Avg
GPRINT:inc_max:MAX:%6.2lf Max
GPRINT:inc_avg:LAST:%6.2lf Last\l
'''

graph_disk_time = r'''
-v
Seconds/s
DEF:out_min_raw={file}:write:MIN
DEF:out_avg_raw={file}:write:AVERAGE
DEF:out_max_raw={file}:write:MAX
DEF:inc_min_raw={file}:read:MIN
DEF:inc_avg_raw={file}:read:AVERAGE
DEF:inc_max_raw={file}:read:MAX
CDEF:out_min=out_min_raw1000/
CDEF:out_avg=out_avg_raw1000/
CDEF:out_max=out_max_raw1000/
CDEF:inc_min=inc_min_raw1000/
CDEF:inc_avg=inc_avg_raw1000/
CDEF:inc_max=inc_max_raw1000/
CDEF:overlap=out_avginc_avgGTinc_avgout_avgIF
AREA:out_avg#{colors[HalfGreen]}
AREA:inc_avg#{colors[HalfBlue]}
AREA:overlap#{colors[HalfBlueGreen]}
LINE1:out_avg#{colors[FullGreen]}:Written
GPRINT:out_avg:AVERAGE:%5.1lf%ss Avg
GPRINT:out_max:MAX:%5.1lf%ss Max
GPRINT:out_avg:LAST:%5.1lf%ss Last\l
LINE1:inc_avg#{colors[FullBlue]}:Read
GPRINT:inc_avg:AVERAGE:%5.1lf%ss Avg
GPRINT:inc_max:MAX:%5.1lf%ss Max
GPRINT:inc_avg:LAST:%5.1lf%ss Last\l
'''

graph_dns_octets = r'''
DEF:rsp_min_raw={file}:responses:MIN
DEF:rsp_avg_raw={file}:responses:AVERAGE
DEF:rsp_max_raw={file}:responses:MAX
DEF:qry_min_raw={file}:queries:MIN
DEF:qry_avg_raw={file}:queries:AVERAGE
DEF:qry_max_raw={file}:queries:MAX
CDEF:rsp_min=rsp_min_raw8*
CDEF:rsp_avg=rsp_avg_raw8*
CDEF:rsp_max=rsp_max_raw8*
CDEF:qry_min=qry_min_raw8*
CDEF:qry_avg=qry_avg_raw8*
CDEF:qry_max=qry_max_raw8*
CDEF:overlap=rsp_avgqry_avgGTqry_avgrsp_avgIF
CDEF:mytime=rsp_avg_rawTIMETIMEIF
CDEF:sample_len_raw=mytimePREV(mytime)-
CDEF:sample_len=sample_len_rawUN0sample_len_rawIF
CDEF:rsp_avg_sample=rsp_avg_rawUN0rsp_avg_rawIFsample_len*
CDEF:rsp_avg_sum=PREVUN0PREVIFrsp_avg_sample+
CDEF:qry_avg_sample=qry_avg_rawUN0qry_avg_rawIFsample_len*
CDEF:qry_avg_sum=PREVUN0PREVIFqry_avg_sample+
AREA:rsp_avg#{colors[HalfGreen]}
AREA:qry_avg#{colors[HalfBlue]}
AREA:overlap#{colors[HalfBlueGreen]}
LINE1:rsp_avg#{colors[FullGreen]}:Responses
GPRINT:rsp_avg:AVERAGE:%5.1lf%s Avg
GPRINT:rsp_max:MAX:%5.1lf%s Max
GPRINT:rsp_avg:LAST:%5.1lf%s Last
GPRINT:rsp_avg_sum:LAST:(ca. %5.1lf%sB Total)\l
LINE1:qry_avg#{colors[FullBlue]}:Queries
#'GPRINT:qry_min:MIN:%5.1lf %s Min'
GPRINT:qry_avg:AVERAGE:%5.1lf%s Avg
GPRINT:qry_max:MAX:%5.1lf%s Max
GPRINT:qry_avg:LAST:%5.1lf%s Last
GPRINT:qry_avg_sum:LAST:(ca. %5.1lf%sB Total)\l
'''

graph_dns_opcode = r'''
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Queries/s
GPRINT:min:MIN:%9.3lf Min
GPRINT:avg:AVERAGE:%9.3lf Average
GPRINT:max:MAX:%9.3lf Max
GPRINT:avg:LAST:%9.3lf Last\l
'''

graph_email_count = r'''
-v
Mails
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfMagenta]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullMagenta]}:Count
GPRINT:min:MIN:%4.1lf Min
GPRINT:avg:AVERAGE:%4.1lf Avg
GPRINT:max:MAX:%4.1lf Max
GPRINT:avg:LAST:%4.1lf Last\l
'''

graph_email_size = r'''
-v
Bytes
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfMagenta]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullMagenta]}:Count
GPRINT:min:MIN:%4.1lf Min
GPRINT:avg:AVERAGE:%4.1lf Avg
GPRINT:max:MAX:%4.1lf Max
GPRINT:avg:LAST:%4.1lf Last\l
'''

graph_spam_score = r'''
-v
Score
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Score
GPRINT:min:MIN:%4.1lf Min
GPRINT:avg:AVERAGE:%4.1lf Avg
GPRINT:max:MAX:%4.1lf Max
GPRINT:avg:LAST:%4.1lf Last\l
'''

graph_spam_check = r'''
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfMagenta]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullMagenta]}:Count
GPRINT:min:MIN:%4.1lf Min
GPRINT:avg:AVERAGE:%4.1lf Avg
GPRINT:max:MAX:%4.1lf Max
GPRINT:avg:LAST:%4.1lf Last\l
'''

graph_conntrack = r'''
-v
Entries
DEF:avg={file}:entropy:AVERAGE
DEF:min={file}:entropy:MIN
DEF:max={file}:entropy:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Count
GPRINT:min:MIN:%4.0lf Min
GPRINT:avg:AVERAGE:%4.0lf Avg
GPRINT:max:MAX:%4.0lf Max
GPRINT:avg:LAST:%4.0lf Last\l
'''

graph_entropy = r'''
-v
Bits
DEF:avg={file}:entropy:AVERAGE
DEF:min={file}:entropy:MIN
DEF:max={file}:entropy:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Bits
GPRINT:min:MIN:%4.0lfbit Min
GPRINT:avg:AVERAGE:%4.0lfbit Avg
GPRINT:max:MAX:%4.0lfbit Max
GPRINT:avg:LAST:%4.0lfbit Last\l
'''

graph_fanspeed = r'''
-v
RPM
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfMagenta]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullMagenta]}:RPM
GPRINT:min:MIN:%4.1lf Min
GPRINT:avg:AVERAGE:%4.1lf Avg
GPRINT:max:MAX:%4.1lf Max
GPRINT:avg:LAST:%4.1lf Last\l
'''

graph_frequency = r'''
-v
Hertz
DEF:avg={file}:frequency:AVERAGE
DEF:min={file}:frequency:MIN
DEF:max={file}:frequency:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Frequency [Hz]
GPRINT:min:MIN:%4.1lf Min
GPRINT:avg:AVERAGE:%4.1lf Avg
GPRINT:max:MAX:%4.1lf Max
GPRINT:avg:LAST:%4.1lf Last\l
'''

graph_frequency_offset = r'''
# NTPd
DEF:ppm_avg={file}:ppm:AVERAGE
DEF:ppm_min={file}:ppm:MIN
DEF:ppm_max={file}:ppm:MAX
AREA:ppm_max#{colors[HalfBlue]}
AREA:ppm_min#{colors[Canvas]}
LINE1:ppm_avg#{colors[FullBlue]}:{inst}
GPRINT:ppm_min:MIN:%5.2lf Min
GPRINT:ppm_avg:AVERAGE:%5.2lf Avg
GPRINT:ppm_max:MAX:%5.2lf Max
GPRINT:ppm_avg:LAST:%5.2lf Last
'''

graph_gauge = r'''
-v
Exec value
DEF:temp_avg={file}:value:AVERAGE
DEF:temp_min={file}:value:MIN
DEF:temp_max={file}:value:MAX
AREA:temp_max#{colors[HalfBlue]}
AREA:temp_min#{colors[Canvas]}
LINE1:temp_avg#{colors[FullBlue]}:Exec value
GPRINT:temp_min:MIN:%6.2lf Min
GPRINT:temp_avg:AVERAGE:%6.2lf Avg
GPRINT:temp_max:MAX:%6.2lf Max
GPRINT:temp_avg:LAST:%6.2lf Last\l
'''

graph_hddtemp = r'''
DEF:temp_avg={file}:value:AVERAGE
DEF:temp_min={file}:value:MIN
DEF:temp_max={file}:value:MAX
AREA:temp_max#{colors[HalfRed]}
AREA:temp_min#{colors[Canvas]}
LINE1:temp_avg#{colors[FullRed]}:Temperature
GPRINT:temp_min:MIN:%4.1lf Min
GPRINT:temp_avg:AVERAGE:%4.1lf Avg
GPRINT:temp_max:MAX:%4.1lf Max
GPRINT:temp_avg:LAST:%4.1lf Last\l
'''

graph_humidity = r'''
-v
Percent
DEF:temp_avg={file}:value:AVERAGE
DEF:temp_min={file}:value:MIN
DEF:temp_max={file}:value:MAX
AREA:temp_max#{colors[HalfGreen]}
AREA:temp_min#{colors[Canvas]}
LINE1:temp_avg#{colors[FullGreen]}:Temperature
GPRINT:temp_min:MIN:%4.1lf%% Min
GPRINT:temp_avg:AVERAGE:%4.1lf%% Avg
GPRINT:temp_max:MAX:%4.1lf%% Max
GPRINT:temp_avg:LAST:%4.1lf%% Last\l
'''

graph_if_errors = r'''
-v
Errors/s
DEF:tx_min={file}:tx:MIN
DEF:tx_avg={file}:tx:AVERAGE
DEF:tx_max={file}:tx:MAX
DEF:rx_min={file}:rx:MIN
DEF:rx_avg={file}:rx:AVERAGE
DEF:rx_max={file}:rx:MAX
CDEF:overlap=tx_avgrx_avgGTrx_avgtx_avgIF
CDEF:mytime=tx_avgTIMETIMEIF
CDEF:sample_len_raw=mytimePREV(mytime)-
CDEF:sample_len=sample_len_rawUN0sample_len_rawIF
CDEF:tx_avg_sample=tx_avgUN0tx_avgIFsample_len*
CDEF:tx_avg_sum=PREVUN0PREVIFtx_avg_sample+
CDEF:rx_avg_sample=rx_avgUN0rx_avgIFsample_len*
CDEF:rx_avg_sum=PREVUN0PREVIFrx_avg_sample+
AREA:tx_avg#{colors[HalfGreen]}
AREA:rx_avg#{colors[HalfBlue]}
AREA:overlap#{colors[HalfBlueGreen]}
LINE1:tx_avg#{colors[FullGreen]}:TX
GPRINT:tx_avg:AVERAGE:%5.1lf%s Avg
GPRINT:tx_max:MAX:%5.1lf%s Max
GPRINT:tx_avg:LAST:%5.1lf%s Last
GPRINT:tx_avg_sum:LAST:(ca. %4.0lf%s Total)\l
LINE1:rx_avg#{colors[FullBlue]}:RX
#'GPRINT:rx_min:MIN:%5.1lf %s Min'
GPRINT:rx_avg:AVERAGE:%5.1lf%s Avg
GPRINT:rx_max:MAX:%5.1lf%s Max
GPRINT:rx_avg:LAST:%5.1lf%s Last
GPRINT:rx_avg_sum:LAST:(ca. %4.0lf%s Total)\l
'''

graph_if_collisions = r'''
-v
Collisions/s
DEF:min_raw={file}:value:MIN
DEF:avg_raw={file}:value:AVERAGE
DEF:max_raw={file}:value:MAX
CDEF:min=min_raw8*
CDEF:avg=avg_raw8*
CDEF:max=max_raw8*
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Collisions/s
GPRINT:min:MIN:%5.1lf %s Min
GPRINT:avg:AVERAGE:%5.1lf%s Avg
GPRINT:max:MAX:%5.1lf%s Max
GPRINT:avg:LAST:%5.1lf%s Last\l
'''

graph_if_dropped = r'''
-v
Packets/s
DEF:tx_min={file}:tx:MIN
DEF:tx_avg={file}:tx:AVERAGE
DEF:tx_max={file}:tx:MAX
DEF:rx_min={file}:rx:MIN
DEF:rx_avg={file}:rx:AVERAGE
DEF:rx_max={file}:rx:MAX
CDEF:overlap=tx_avgrx_avgGTrx_avgtx_avgIF
CDEF:mytime=tx_avgTIMETIMEIF
CDEF:sample_len_raw=mytimePREV(mytime)-
CDEF:sample_len=sample_len_rawUN0sample_len_rawIF
CDEF:tx_avg_sample=tx_avgUN0tx_avgIFsample_len*
CDEF:tx_avg_sum=PREVUN0PREVIFtx_avg_sample+
CDEF:rx_avg_sample=rx_avgUN0rx_avgIFsample_len*
CDEF:rx_avg_sum=PREVUN0PREVIFrx_avg_sample+
AREA:tx_avg#{colors[HalfGreen]}
AREA:rx_avg#{colors[HalfBlue]}
AREA:overlap#{colors[HalfBlueGreen]}
LINE1:tx_avg#{colors[FullGreen]}:TX
GPRINT:tx_avg:AVERAGE:%5.1lf%s Avg
GPRINT:tx_max:MAX:%5.1lf%s Max
GPRINT:tx_avg:LAST:%5.1lf%s Last
GPRINT:tx_avg_sum:LAST:(ca. %4.0lf%s Total)\l
LINE1:rx_avg#{colors[FullBlue]}:RX
#'GPRINT:rx_min:MIN:%5.1lf %s Min'
GPRINT:rx_avg:AVERAGE:%5.1lf%s Avg
GPRINT:rx_max:MAX:%5.1lf%s Max
GPRINT:rx_avg:LAST:%5.1lf%s Last
GPRINT:rx_avg_sum:LAST:(ca. %4.0lf%s Total)\l
'''

graph_if_packets = r'''
-v
Packets/s
DEF:tx_min={file}:tx:MIN
DEF:tx_avg={file}:tx:AVERAGE
DEF:tx_max={file}:tx:MAX
DEF:rx_min={file}:rx:MIN
DEF:rx_avg={file}:rx:AVERAGE
DEF:rx_max={file}:rx:MAX
CDEF:overlap=tx_avgrx_avgGTrx_avgtx_avgIF
CDEF:mytime=tx_avgTIMETIMEIF
CDEF:sample_len_raw=mytimePREV(mytime)-
CDEF:sample_len=sample_len_rawUN0sample_len_rawIF
CDEF:tx_avg_sample=tx_avgUN0tx_avgIFsample_len*
CDEF:tx_avg_sum=PREVUN0PREVIFtx_avg_sample+
CDEF:rx_avg_sample=rx_avgUN0rx_avgIFsample_len*
CDEF:rx_avg_sum=PREVUN0PREVIFrx_avg_sample+
AREA:tx_avg#{colors[HalfGreen]}
AREA:rx_avg#{colors[HalfBlue]}
AREA:overlap#{colors[HalfBlueGreen]}
LINE1:tx_avg#{colors[FullGreen]}:TX
GPRINT:tx_avg:AVERAGE:%5.1lf%s Avg
GPRINT:tx_max:MAX:%5.1lf%s Max
GPRINT:tx_avg:LAST:%5.1lf%s Last
GPRINT:tx_avg_sum:LAST:(ca. %4.0lf%s Total)\l
LINE1:rx_avg#{colors[FullBlue]}:RX
#'GPRINT:rx_min:MIN:%5.1lf %s Min'
GPRINT:rx_avg:AVERAGE:%5.1lf%s Avg
GPRINT:rx_max:MAX:%5.1lf%s Max
GPRINT:rx_avg:LAST:%5.1lf%s Last
GPRINT:rx_avg_sum:LAST:(ca. %4.0lf%s Total)\l
'''

graph_if_rx_errors = r'''
-v
Errors/s
DEF:min={file}:value:MIN
DEF:avg={file}:value:AVERAGE
DEF:max={file}:value:MAX
CDEF:mytime=avgTIMETIMEIF
CDEF:sample_len_raw=mytimePREV(mytime)-
CDEF:sample_len=sample_len_rawUN0sample_len_rawIF
CDEF:avg_sample=avgUN0avgIFsample_len*
CDEF:avg_sum=PREVUN0PREVIFavg_sample+
AREA:avg#{colors[HalfBlue]}
LINE1:avg#{colors[FullBlue]}:Errors/s
GPRINT:avg:AVERAGE:%3.1lf%s Avg
GPRINT:max:MAX:%3.1lf%s Max
GPRINT:avg:LAST:%3.1lf%s Last
GPRINT:avg_sum:LAST:(ca. %2.0lf%s Total)\l
'''

graph_ipt_bytes = r'''
-v
Bits/s
DEF:min_raw={file}:value:MIN
DEF:avg_raw={file}:value:AVERAGE
DEF:max_raw={file}:value:MAX
CDEF:min=min_raw8*
CDEF:avg=avg_raw8*
CDEF:max=max_raw8*
CDEF:mytime=avg_rawTIMETIMEIF
CDEF:sample_len_raw=mytimePREV(mytime)-
CDEF:sample_len=sample_len_rawUN0sample_len_rawIF
CDEF:avg_sample=avg_rawUN0avg_rawIFsample_len*
CDEF:avg_sum=PREVUN0PREVIFavg_sample+
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Bits/s
#'GPRINT:min:MIN:%5.1lf %s Min'
GPRINT:avg:AVERAGE:%5.1lf%s Avg
GPRINT:max:MAX:%5.1lf%s Max
GPRINT:avg:LAST:%5.1lf%s Last
GPRINT:avg_sum:LAST:(ca. %5.1lf%sB Total)\l
'''

graph_ipt_packets = r'''
-v
Packets/s
DEF:min_raw={file}:value:MIN
DEF:avg_raw={file}:value:AVERAGE
DEF:max_raw={file}:value:MAX
CDEF:min=min_raw8*
CDEF:avg=avg_raw8*
CDEF:max=max_raw8*
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Packets/s
GPRINT:min:MIN:%5.1lf %s Min
GPRINT:avg:AVERAGE:%5.1lf%s Avg
GPRINT:max:MAX:%5.1lf%s Max
GPRINT:avg:LAST:%5.1lf%s Last\l
'''

graph_irq = r'''
-v
Issues/s
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Issues/s
GPRINT:min:MIN:%6.2lf Min
GPRINT:avg:AVERAGE:%6.2lf Avg
GPRINT:max:MAX:%6.2lf Max
GPRINT:avg:LAST:%6.2lf Last\l
'''

graph_load = r'''
-v
System load
DEF:s_avg={file}:shortterm:AVERAGE
DEF:s_min={file}:shortterm:MIN
DEF:s_max={file}:shortterm:MAX
DEF:m_avg={file}:midterm:AVERAGE
DEF:m_min={file}:midterm:MIN
DEF:m_max={file}:midterm:MAX
DEF:l_avg={file}:longterm:AVERAGE
DEF:l_min={file}:longterm:MIN
DEF:l_max={file}:longterm:MAX
AREA:s_max#{colors[HalfGreen]}
AREA:s_min#{colors[Canvas]}
LINE1:s_avg#{colors[FullGreen]}: 1m average
GPRINT:s_min:MIN:%4.2lf Min
GPRINT:s_avg:AVERAGE:%4.2lf Avg
GPRINT:s_max:MAX:%4.2lf Max
GPRINT:s_avg:LAST:%4.2lf Last\n
LINE1:m_avg#{colors[FullBlue]}: 5m average
GPRINT:m_min:MIN:%4.2lf Min
GPRINT:m_avg:AVERAGE:%4.2lf Avg
GPRINT:m_max:MAX:%4.2lf Max
GPRINT:m_avg:LAST:%4.2lf Last\n
LINE1:l_avg#{colors[FullRed]}:15m average
GPRINT:l_min:MIN:%4.2lf Min
GPRINT:l_avg:AVERAGE:%4.2lf Avg
GPRINT:l_max:MAX:%4.2lf Max
GPRINT:l_avg:LAST:%4.2lf Last
'''

graph_load_percent = r'''
DEF:avg={file}:percent:AVERAGE
DEF:min={file}:percent:MIN
DEF:max={file}:percent:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Load
GPRINT:min:MIN:%5.1lf%s%% Min
GPRINT:avg:AVERAGE:%5.1lf%s%% Avg
GPRINT:max:MAX:%5.1lf%s%% Max
GPRINT:avg:LAST:%5.1lf%s%% Last\l
'''

graph_mails = r'''
DEF:rawgood={file}:good:AVERAGE
DEF:rawspam={file}:spam:AVERAGE
CDEF:good=rawgoodUN0rawgoodIF
CDEF:spam=rawspamUN0rawspamIF
CDEF:negspam=spam-1*
AREA:good#{colors[HalfGreen]}
LINE1:good#{colors[FullGreen]}:Good mails
GPRINT:good:AVERAGE:%4.1lf Avg
GPRINT:good:MAX:%4.1lf Max
GPRINT:good:LAST:%4.1lf Last\n
AREA:negspam#{colors[HalfRed]}
LINE1:negspam#{colors[FullRed]}:Spam mails
GPRINT:spam:AVERAGE:%4.1lf Avg
GPRINT:spam:MAX:%4.1lf Max
GPRINT:spam:LAST:%4.1lf Last
HRULE:0#000000
'''

graph_memcached_command = r'''
-v
Commands
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Commands
GPRINT:min:MIN:%5.1lf%s Min
GPRINT:avg:AVERAGE:%5.1lf Avg
GPRINT:max:MAX:%5.1lf Max
GPRINT:avg:LAST:%5.1lf Last\l
'''

graph_memcached_connections = r'''
-v
Connections
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Connections
GPRINT:min:MIN:%4.1lf Min
GPRINT:avg:AVERAGE:%4.1lf Avg
GPRINT:max:MAX:%4.1lf Max
GPRINT:avg:LAST:%4.1lf Last\l
'''

graph_memcached_items = r'''
-v
Items
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Items
GPRINT:min:MIN:%4.1lf Min
GPRINT:avg:AVERAGE:%4.1lf Avg
GPRINT:max:MAX:%4.1lf Max
GPRINT:avg:LAST:%4.1lf Last\l
'''

graph_memcached_octets = r'''
-v
Bits/s
DEF:out_min={file}:tx:MIN
DEF:out_avg={file}:tx:AVERAGE
DEF:out_max={file}:tx:MAX
DEF:inc_min={file}:rx:MIN
DEF:inc_avg={file}:rx:AVERAGE
DEF:inc_max={file}:rx:MAX
CDEF:mytime=out_avgTIMETIMEIF
CDEF:sample_len_raw=mytimePREV(mytime)-
CDEF:sample_len=sample_len_rawUN0sample_len_rawIF
CDEF:out_avg_sample=out_avgUN0out_avgIFsample_len*
CDEF:out_avg_sum=PREVUN0PREVIFout_avg_sample+
CDEF:inc_avg_sample=inc_avgUN0inc_avgIFsample_len*
CDEF:inc_avg_sum=PREVUN0PREVIFinc_avg_sample+
CDEF:out_bit_min=out_min8*
CDEF:out_bit_avg=out_avg8*
CDEF:out_bit_max=out_max8*
CDEF:inc_bit_min=inc_min8*
CDEF:inc_bit_avg=inc_avg8*
CDEF:inc_bit_max=inc_max8*
CDEF:overlap=out_bit_avginc_bit_avgGTinc_bit_avgout_bit_avgIF
AREA:out_bit_avg#{colors[HalfGreen]}
AREA:inc_bit_avg#{colors[HalfBlue]}
AREA:overlap#{colors[HalfBlueGreen]}
LINE1:out_bit_avg#{colors[FullGreen]}:Written
GPRINT:out_bit_avg:AVERAGE:%5.1lf%s Avg
GPRINT:out_bit_max:MAX:%5.1lf%s Max
GPRINT:out_bit_avg:LAST:%5.1lf%s Last
GPRINT:out_avg_sum:LAST:(ca. %5.1lf%sB Total)\l
LINE1:inc_bit_avg#{colors[FullBlue]}:Read
GPRINT:inc_bit_avg:AVERAGE:%5.1lf%s Avg
GPRINT:inc_bit_max:MAX:%5.1lf%s Max
GPRINT:inc_bit_avg:LAST:%5.1lf%s Last
GPRINT:inc_avg_sum:LAST:(ca. %5.1lf%sB Total)\l
'''

graph_memcached_ops = r'''
-v
Ops
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Ops
GPRINT:min:MIN:%4.1lf Min
GPRINT:avg:AVERAGE:%4.1lf Avg
GPRINT:max:MAX:%4.1lf Max
GPRINT:avg:LAST:%4.1lf Last\l
'''

graph_memory = r'''
-b
1024
-v
Bytes
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Memory
GPRINT:min:MIN:%5.1lf%sbyte Min
GPRINT:avg:AVERAGE:%5.1lf%sbyte Avg
GPRINT:max:MAX:%5.1lf%sbyte Max
GPRINT:avg:LAST:%5.1lf%sbyte Last\l
'''

graph_old_memory = r'''
DEF:used_avg={file}:used:AVERAGE
DEF:free_avg={file}:free:AVERAGE
DEF:buffers_avg={file}:buffers:AVERAGE
DEF:cached_avg={file}:cached:AVERAGE
DEF:used_min={file}:used:MIN
DEF:free_min={file}:free:MIN
DEF:buffers_min={file}:buffers:MIN
DEF:cached_min={file}:cached:MIN
DEF:used_max={file}:used:MAX
DEF:free_max={file}:free:MAX
DEF:buffers_max={file}:buffers:MAX
DEF:cached_max={file}:cached:MAX
CDEF:cached_avg_nn=cached_avgUN0cached_avgIF
CDEF:buffers_avg_nn=buffers_avgUN0buffers_avgIF
CDEF:free_cached_buffers_used=free_avgcached_avg_nn+buffers_avg_nn+used_avg+
CDEF:cached_buffers_used=cached_avgbuffers_avg_nn+used_avg+
CDEF:buffers_used=buffers_avgused_avg+
AREA:free_cached_buffers_used#{colors[HalfGreen]}
AREA:cached_buffers_used#{colors[HalfBlue]}
AREA:buffers_used#{colors[HalfYellow]}
AREA:used_avg#{colors[HalfRed]}
LINE1:free_cached_buffers_used#{colors[FullGreen]}:Free
GPRINT:free_min:MIN:%5.1lf%s Min
GPRINT:free_avg:AVERAGE:%5.1lf%s Avg
GPRINT:free_max:MAX:%5.1lf%s Max
GPRINT:free_avg:LAST:%5.1lf%s Last\n
LINE1:cached_buffers_used#{colors[FullBlue]}:Page cache
GPRINT:cached_min:MIN:%5.1lf%s Min
GPRINT:cached_avg:AVERAGE:%5.1lf%s Avg
GPRINT:cached_max:MAX:%5.1lf%s Max
GPRINT:cached_avg:LAST:%5.1lf%s Last\n
LINE1:buffers_used#{colors[FullYellow]}:Buffer cache
GPRINT:buffers_min:MIN:%5.1lf%s Min
GPRINT:buffers_avg:AVERAGE:%5.1lf%s Avg
GPRINT:buffers_max:MAX:%5.1lf%s Max
GPRINT:buffers_avg:LAST:%5.1lf%s Last\n
LINE1:used_avg#{colors[FullRed]}:Used
GPRINT:used_min:MIN:%5.1lf%s Min
GPRINT:used_avg:AVERAGE:%5.1lf%s Avg
GPRINT:used_max:MAX:%5.1lf%s Max
GPRINT:used_avg:LAST:%5.1lf%s Last
'''

graph_mysql_commands = r'''
-v
Issues/s
DEF:val_avg={file}:value:AVERAGE
DEF:val_min={file}:value:MIN
DEF:val_max={file}:value:MAX
AREA:val_max#{colors[HalfBlue]}
AREA:val_min#{colors[Canvas]}
LINE1:val_avg#{colors[FullBlue]}:Issues/s
GPRINT:val_min:MIN:%5.2lf Min
GPRINT:val_avg:AVERAGE:%5.2lf Avg
GPRINT:val_max:MAX:%5.2lf Max
GPRINT:val_avg:LAST:%5.2lf Last
'''

graph_mysql_handler = r'''
-v
Issues/s
DEF:val_avg={file}:value:AVERAGE
DEF:val_min={file}:value:MIN
DEF:val_max={file}:value:MAX
AREA:val_max#{colors[HalfBlue]}
AREA:val_min#{colors[Canvas]}
LINE1:val_avg#{colors[FullBlue]}:Issues/s
GPRINT:val_min:MIN:%5.2lf Min
GPRINT:val_avg:AVERAGE:%5.2lf Avg
GPRINT:val_max:MAX:%5.2lf Max
GPRINT:val_avg:LAST:%5.2lf Last
'''

graph_mysql_octets = r'''
-v
Bits/s
DEF:out_min={file}:tx:MIN
DEF:out_avg={file}:tx:AVERAGE
DEF:out_max={file}:tx:MAX
DEF:inc_min={file}:rx:MIN
DEF:inc_avg={file}:rx:AVERAGE
DEF:inc_max={file}:rx:MAX
CDEF:mytime=out_avgTIMETIMEIF
CDEF:sample_len_raw=mytimePREV(mytime)-
CDEF:sample_len=sample_len_rawUN0sample_len_rawIF
CDEF:out_avg_sample=out_avgUN0out_avgIFsample_len*
CDEF:out_avg_sum=PREVUN0PREVIFout_avg_sample+
CDEF:inc_avg_sample=inc_avgUN0inc_avgIFsample_len*
CDEF:inc_avg_sum=PREVUN0PREVIFinc_avg_sample+
CDEF:out_bit_min=out_min8*
CDEF:out_bit_avg=out_avg8*
CDEF:out_bit_max=out_max8*
CDEF:inc_bit_min=inc_min8*
CDEF:inc_bit_avg=inc_avg8*
CDEF:inc_bit_max=inc_max8*
CDEF:overlap=out_bit_avginc_bit_avgGTinc_bit_avgout_bit_avgIF
AREA:out_bit_avg#{colors[HalfGreen]}
AREA:inc_bit_avg#{colors[HalfBlue]}
AREA:overlap#{colors[HalfBlueGreen]}
LINE1:out_bit_avg#{colors[FullGreen]}:Written
GPRINT:out_bit_avg:AVERAGE:%5.1lf%s Avg
GPRINT:out_bit_max:MAX:%5.1lf%s Max
GPRINT:out_bit_avg:LAST:%5.1lf%s Last
GPRINT:out_avg_sum:LAST:(ca. %5.1lf%sB Total)\l
LINE1:inc_bit_avg#{colors[FullBlue]}:Read
GPRINT:inc_bit_avg:AVERAGE:%5.1lf%s Avg
GPRINT:inc_bit_max:MAX:%5.1lf%s Max
GPRINT:inc_bit_avg:LAST:%5.1lf%s Last
GPRINT:inc_avg_sum:LAST:(ca. %5.1lf%sB Total)\l
'''

graph_mysql_qcache = r'''
-v
Queries/s
DEF:hits_min={file}:hits:MIN
DEF:hits_avg={file}:hits:AVERAGE
DEF:hits_max={file}:hits:MAX
DEF:inserts_min={file}:inserts:MIN
DEF:inserts_avg={file}:inserts:AVERAGE
DEF:inserts_max={file}:inserts:MAX
DEF:not_cached_min={file}:not_cached:MIN
DEF:not_cached_avg={file}:not_cached:AVERAGE
DEF:not_cached_max={file}:not_cached:MAX
DEF:lowmem_prunes_min={file}:lowmem_prunes:MIN
DEF:lowmem_prunes_avg={file}:lowmem_prunes:AVERAGE
DEF:lowmem_prunes_max={file}:lowmem_prunes:MAX
DEF:queries_min={file}:queries_in_cache:MIN
DEF:queries_avg={file}:queries_in_cache:AVERAGE
DEF:queries_max={file}:queries_in_cache:MAX
CDEF:unknown=queries_avgUNKN+
CDEF:not_cached_agg=hits_avginserts_avg+not_cached_avg+
CDEF:inserts_agg=hits_avginserts_avg+
CDEF:hits_agg=hits_avg
AREA:not_cached_agg#{colors[HalfYellow]}
AREA:inserts_agg#{colors[HalfBlue]}
AREA:hits_agg#{colors[HalfGreen]}
LINE1:not_cached_agg#{colors[FullYellow]}:Not Cached
GPRINT:not_cached_min:MIN:%5.2lf Min
GPRINT:not_cached_avg:AVERAGE:%5.2lf Avg
GPRINT:not_cached_max:MAX:%5.2lf Max
GPRINT:not_cached_avg:LAST:%5.2lf Last\l
LINE1:inserts_agg#{colors[FullBlue]}:Inserts
GPRINT:inserts_min:MIN:%5.2lf Min
GPRINT:inserts_avg:AVERAGE:%5.2lf Avg
GPRINT:inserts_max:MAX:%5.2lf Max
GPRINT:inserts_avg:LAST:%5.2lf Last\l
LINE1:hits_agg#{colors[FullGreen]}:Hits
GPRINT:hits_min:MIN:%5.2lf Min
GPRINT:hits_avg:AVERAGE:%5.2lf Avg
GPRINT:hits_max:MAX:%5.2lf Max
GPRINT:hits_avg:LAST:%5.2lf Last\l
LINE1:lowmem_prunes_avg#{colors[FullRed]}:Lowmem Prunes
GPRINT:lowmem_prunes_min:MIN:%5.2lf Min
GPRINT:lowmem_prunes_avg:AVERAGE:%5.2lf Avg
GPRINT:lowmem_prunes_max:MAX:%5.2lf Max
GPRINT:lowmem_prunes_avg:LAST:%5.2lf Last\l
LINE1:unknown#{colors[Canvas]}:Queries in cache
GPRINT:queries_min:MIN:%5.0lf Min
GPRINT:queries_avg:AVERAGE:%5.0lf Avg
GPRINT:queries_max:MAX:%5.0lf Max
GPRINT:queries_avg:LAST:%5.0lf Last\l
'''

graph_mysql_threads = r'''
-v
Threads
DEF:running_min={file}:running:MIN
DEF:running_avg={file}:running:AVERAGE
DEF:running_max={file}:running:MAX
DEF:connected_min={file}:connected:MIN
DEF:connected_avg={file}:connected:AVERAGE
DEF:connected_max={file}:connected:MAX
DEF:cached_min={file}:cached:MIN
DEF:cached_avg={file}:cached:AVERAGE
DEF:cached_max={file}:cached:MAX
DEF:created_min={file}:created:MIN
DEF:created_avg={file}:created:AVERAGE
DEF:created_max={file}:created:MAX
CDEF:unknown=created_avgUNKN+
CDEF:cached_agg=connected_avgcached_avg+
AREA:cached_agg#{colors[HalfGreen]}
AREA:connected_avg#{colors[HalfBlue]}
AREA:running_avg#{colors[HalfRed]}
LINE1:cached_agg#{colors[FullGreen]}:Cached
GPRINT:cached_min:MIN:%5.1lf Min
GPRINT:cached_avg:AVERAGE:%5.1lf Avg
GPRINT:cached_max:MAX:%5.1lf Max
GPRINT:cached_avg:LAST:%5.1lf Last\l
LINE1:connected_avg#{colors[FullBlue]}:Connected
GPRINT:connected_min:MIN:%5.1lf Min
GPRINT:connected_avg:AVERAGE:%5.1lf Avg
GPRINT:connected_max:MAX:%5.1lf Max
GPRINT:connected_avg:LAST:%5.1lf Last\l
LINE1:running_avg#{colors[FullRed]}:Running
GPRINT:running_min:MIN:%5.1lf Min
GPRINT:running_avg:AVERAGE:%5.1lf Avg
GPRINT:running_max:MAX:%5.1lf Max
GPRINT:running_avg:LAST:%5.1lf Last\l
LINE1:unknown#{colors[Canvas]}:Created
GPRINT:created_min:MIN:%5.0lf Min
GPRINT:created_avg:AVERAGE:%5.0lf Avg
GPRINT:created_max:MAX:%5.0lf Max
GPRINT:created_avg:LAST:%5.0lf Last\l
'''

graph_nfs_procedure = r'''
-v
Issues/s
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Issues/s
GPRINT:min:MIN:%6.2lf Min
GPRINT:avg:AVERAGE:%6.2lf Avg
GPRINT:max:MAX:%6.2lf Max
GPRINT:avg:LAST:%6.2lf Last\l
'''

graph_nfs3_procedures = r'''
DEF:null_avg={file}:null:AVERAGE
DEF:getattr_avg={file}:getattr:AVERAGE
DEF:setattr_avg={file}:setattr:AVERAGE
DEF:lookup_avg={file}:lookup:AVERAGE
DEF:access_avg={file}:access:AVERAGE
DEF:readlink_avg={file}:readlink:AVERAGE
DEF:read_avg={file}:read:AVERAGE
DEF:write_avg={file}:write:AVERAGE
DEF:create_avg={file}:create:AVERAGE
DEF:mkdir_avg={file}:mkdir:AVERAGE
DEF:symlink_avg={file}:symlink:AVERAGE
DEF:mknod_avg={file}:mknod:AVERAGE
DEF:remove_avg={file}:remove:AVERAGE
DEF:rmdir_avg={file}:rmdir:AVERAGE
DEF:rename_avg={file}:rename:AVERAGE
DEF:link_avg={file}:link:AVERAGE
DEF:readdir_avg={file}:readdir:AVERAGE
DEF:readdirplus_avg={file}:readdirplus:AVERAGE
DEF:fsstat_avg={file}:fsstat:AVERAGE
DEF:fsinfo_avg={file}:fsinfo:AVERAGE
DEF:pathconf_avg={file}:pathconf:AVERAGE
DEF:commit_avg={file}:commit:AVERAGE
DEF:null_max={file}:null:MAX
DEF:getattr_max={file}:getattr:MAX
DEF:setattr_max={file}:setattr:MAX
DEF:lookup_max={file}:lookup:MAX
DEF:access_max={file}:access:MAX
DEF:readlink_max={file}:readlink:MAX
DEF:read_max={file}:read:MAX
DEF:write_max={file}:write:MAX
DEF:create_max={file}:create:MAX
DEF:mkdir_max={file}:mkdir:MAX
DEF:symlink_max={file}:symlink:MAX
DEF:mknod_max={file}:mknod:MAX
DEF:remove_max={file}:remove:MAX
DEF:rmdir_max={file}:rmdir:MAX
DEF:rename_max={file}:rename:MAX
DEF:link_max={file}:link:MAX
DEF:readdir_max={file}:readdir:MAX
DEF:readdirplus_max={file}:readdirplus:MAX
DEF:fsstat_max={file}:fsstat:MAX
DEF:fsinfo_max={file}:fsinfo:MAX
DEF:pathconf_max={file}:pathconf:MAX
DEF:commit_max={file}:commit:MAX
CDEF:other_avg=null_avgreadlink_avgcreate_avgmkdir_avgsymlink_avgmknod_avgremove_avgrmdir_avgrename_avglink_avgreaddir_avgreaddirplus_avgfsstat_avgfsinfo_avgpathconf_avg++++++++++++++
CDEF:other_max=null_maxreadlink_maxcreate_maxmkdir_maxsymlink_maxmknod_maxremove_maxrmdir_maxrename_maxlink_maxreaddir_maxreaddirplus_maxfsstat_maxfsinfo_maxpathconf_max++++++++++++++
CDEF:stack_read=read_avg
CDEF:stack_getattr=stack_readgetattr_avg+
CDEF:stack_access=stack_getattraccess_avg+
CDEF:stack_lookup=stack_accesslookup_avg+
CDEF:stack_write=stack_lookupwrite_avg+
CDEF:stack_commit=stack_writecommit_avg+
CDEF:stack_setattr=stack_commitsetattr_avg+
CDEF:stack_other=stack_setattrother_avg+
AREA:stack_other#{colors[HalfRed]}
AREA:stack_setattr#{colors[HalfGreen]}
AREA:stack_commit#{colors[HalfYellow]}
AREA:stack_write#{colors[HalfGreen]}
AREA:stack_lookup#{colors[HalfBlue]}
AREA:stack_access#{colors[HalfMagenta]}
AREA:stack_getattr#{colors[HalfCyan]}
AREA:stack_read#{colors[HalfBlue]}
LINE1:stack_other#{colors[FullRed]}:Other
GPRINT:other_max:MAX:%5.1lf Max
GPRINT:other_avg:AVERAGE:%5.1lf Avg
GPRINT:other_avg:LAST:%5.1lf Last\l
LINE1:stack_setattr#{colors[FullGreen]}:setattr
GPRINT:setattr_max:MAX:%5.1lf Max
GPRINT:setattr_avg:AVERAGE:%5.1lf Avg
GPRINT:setattr_avg:LAST:%5.1lf Last\l
LINE1:stack_commit#{colors[FullYellow]}:commit
GPRINT:commit_max:MAX:%5.1lf Max
GPRINT:commit_avg:AVERAGE:%5.1lf Avg
GPRINT:commit_avg:LAST:%5.1lf Last\l
LINE1:stack_write#{colors[FullGreen]}:write
GPRINT:write_max:MAX:%5.1lf Max
GPRINT:write_avg:AVERAGE:%5.1lf Avg
GPRINT:write_avg:LAST:%5.1lf Last\l
LINE1:stack_lookup#{colors[FullBlue]}:lookup
GPRINT:lookup_max:MAX:%5.1lf Max
GPRINT:lookup_avg:AVERAGE:%5.1lf Avg
GPRINT:lookup_avg:LAST:%5.1lf Last\l
LINE1:stack_access#{colors[FullMagenta]}:access
GPRINT:access_max:MAX:%5.1lf Max
GPRINT:access_avg:AVERAGE:%5.1lf Avg
GPRINT:access_avg:LAST:%5.1lf Last\l
LINE1:stack_getattr#{colors[FullCyan]}:getattr
GPRINT:getattr_max:MAX:%5.1lf Max
GPRINT:getattr_avg:AVERAGE:%5.1lf Avg
GPRINT:getattr_avg:LAST:%5.1lf Last\l
LINE1:stack_read#{colors[FullBlue]}:read
GPRINT:read_max:MAX:%5.1lf Max
GPRINT:read_avg:AVERAGE:%5.1lf Avg
GPRINT:read_avg:LAST:%5.1lf Last\l
'''

graph_partition = r'''
DEF:rbyte_avg={file}:rbytes:AVERAGE
DEF:rbyte_min={file}:rbytes:MIN
DEF:rbyte_max={file}:rbytes:MAX
DEF:wbyte_avg={file}:wbytes:AVERAGE
DEF:wbyte_min={file}:wbytes:MIN
DEF:wbyte_max={file}:wbytes:MAX
CDEF:overlap=wbyte_avgrbyte_avgGTrbyte_avgwbyte_avgIF
AREA:wbyte_avg#{colors[HalfGreen]}
AREA:rbyte_avg#{colors[HalfBlue]}
AREA:overlap#{colors[HalfBlueGreen]}
LINE1:wbyte_avg#{colors[FullGreen]}:Write
GPRINT:wbyte_min:MIN:%5.1lf%s Min
GPRINT:wbyte_avg:AVERAGE:%5.1lf%s Avg
GPRINT:wbyte_max:MAX:%5.1lf%s Max
GPRINT:wbyte_avg:LAST:%5.1lf%s Last\l
LINE1:rbyte_avg#{colors[FullBlue]}:Read
GPRINT:rbyte_min:MIN:%5.1lf%s Min
GPRINT:rbyte_avg:AVERAGE:%5.1lf%s Avg
GPRINT:rbyte_max:MAX:%5.1lf%s Max
GPRINT:rbyte_avg:LAST:%5.1lf%s Last\l
'''

graph_percent = r'''
-v
Percent
DEF:avg={file}:percent:AVERAGE
DEF:min={file}:percent:MIN
DEF:max={file}:percent:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Percent
GPRINT:min:MIN:%5.1lf%% Min
GPRINT:avg:AVERAGE:%5.1lf%% Avg
GPRINT:max:MAX:%5.1lf%% Max
GPRINT:avg:LAST:%5.1lf%% Last\l
'''

graph_ping = r'''
DEF:ping_avg={file}:ping:AVERAGE
DEF:ping_min={file}:ping:MIN
DEF:ping_max={file}:ping:MAX
AREA:ping_max#{colors[HalfBlue]}
AREA:ping_min#{colors[Canvas]}
LINE1:ping_avg#{colors[FullBlue]}:Ping
GPRINT:ping_min:MIN:%4.1lf ms Min
GPRINT:ping_avg:AVERAGE:%4.1lf ms Avg
GPRINT:ping_max:MAX:%4.1lf ms Max
GPRINT:ping_avg:LAST:%4.1lf ms Last
'''

graph_pg_blks = r'''
DEF:pg_blks_avg={file}:value:AVERAGE
DEF:pg_blks_min={file}:value:MIN
DEF:pg_blks_max={file}:value:MAX
AREA:pg_blks_max#{colors[HalfBlue]}
AREA:pg_blks_min#{colors[Canvas]}
LINE1:pg_blks_avg#{colors[FullBlue]}:Blocks
GPRINT:pg_blks_min:MIN:%4.1lf%s Min
GPRINT:pg_blks_avg:AVERAGE:%4.1lf%s Avg
GPRINT:pg_blks_max:MAX:%4.1lf%s Max
GPRINT:pg_blks_avg:LAST:%4.1lf%s Last
'''

graph_pg_db_size = r'''
DEF:pg_db_size_avg={file}:value:AVERAGE
DEF:pg_db_size_min={file}:value:MIN
DEF:pg_db_size_max={file}:value:MAX
AREA:pg_db_size_max#{colors[HalfBlue]}
AREA:pg_db_size_min#{colors[Canvas]}
LINE1:pg_db_size_avg#{colors[FullBlue]}:Bytes
GPRINT:pg_db_size_min:MIN:%4.1lf%s Min
GPRINT:pg_db_size_avg:AVERAGE:%4.1lf%s Avg
GPRINT:pg_db_size_max:MAX:%4.1lf%s Max
GPRINT:pg_db_size_avg:LAST:%4.1lf%s Last
'''

graph_pg_n_tup_c = r'''
DEF:pg_n_tup_avg={file}:value:AVERAGE
DEF:pg_n_tup_min={file}:value:MIN
DEF:pg_n_tup_max={file}:value:MAX
AREA:pg_n_tup_max#{colors[HalfBlue]}
AREA:pg_n_tup_min#{colors[Canvas]}
LINE1:pg_n_tup_avg#{colors[FullBlue]}:Tuples
GPRINT:pg_n_tup_min:MIN:%4.1lf%s Min
GPRINT:pg_n_tup_avg:AVERAGE:%4.1lf%s Avg
GPRINT:pg_n_tup_max:MAX:%4.1lf%s Max
GPRINT:pg_n_tup_avg:LAST:%4.1lf%s Last
'''

graph_pg_n_tup_g = r'''
DEF:pg_n_tup_avg={file}:value:AVERAGE
DEF:pg_n_tup_min={file}:value:MIN
DEF:pg_n_tup_max={file}:value:MAX
AREA:pg_n_tup_max#{colors[HalfBlue]}
AREA:pg_n_tup_min#{colors[Canvas]}
LINE1:pg_n_tup_avg#{colors[FullBlue]}:Tuples
GPRINT:pg_n_tup_min:MIN:%4.1lf%s Min
GPRINT:pg_n_tup_avg:AVERAGE:%4.1lf%s Avg
GPRINT:pg_n_tup_max:MAX:%4.1lf%s Max
GPRINT:pg_n_tup_avg:LAST:%4.1lf%s Last
'''

graph_pg_numbackends = r'''
DEF:pg_numbackends_avg={file}:value:AVERAGE
DEF:pg_numbackends_min={file}:value:MIN
DEF:pg_numbackends_max={file}:value:MAX
AREA:pg_numbackends_max#{colors[HalfBlue]}
AREA:pg_numbackends_min#{colors[Canvas]}
LINE1:pg_numbackends_avg#{colors[FullBlue]}:Backends
GPRINT:pg_numbackends_min:MIN:%4.1lf%s Min
GPRINT:pg_numbackends_avg:AVERAGE:%4.1lf%s Avg
GPRINT:pg_numbackends_max:MAX:%4.1lf%s Max
GPRINT:pg_numbackends_avg:LAST:%4.1lf%s Last
'''

graph_pg_scan = r'''
DEF:pg_scan_avg={file}:value:AVERAGE
DEF:pg_scan_min={file}:value:MIN
DEF:pg_scan_max={file}:value:MAX
AREA:pg_scan_max#{colors[HalfBlue]}
AREA:pg_scan_min#{colors[Canvas]}
LINE1:pg_scan_avg#{colors[FullBlue]}:Scans
GPRINT:pg_scan_min:MIN:%4.1lf%s Min
GPRINT:pg_scan_avg:AVERAGE:%4.1lf%s Avg
GPRINT:pg_scan_max:MAX:%4.1lf%s Max
GPRINT:pg_scan_avg:LAST:%4.1lf%s Last
'''

graph_pg_xact = r'''
DEF:pg_xact_avg={file}:value:AVERAGE
DEF:pg_xact_min={file}:value:MIN
DEF:pg_xact_max={file}:value:MAX
AREA:pg_xact_max#{colors[HalfBlue]}
AREA:pg_xact_min#{colors[Canvas]}
LINE1:pg_xact_avg#{colors[FullBlue]}:Transactions
GPRINT:pg_xact_min:MIN:%4.1lf%s Min
GPRINT:pg_xact_avg:AVERAGE:%4.1lf%s Avg
GPRINT:pg_xact_max:MAX:%4.1lf%s Max
GPRINT:pg_xact_avg:LAST:%4.1lf%s Last
'''

graph_power = r'''
-v
Watt
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Watt
GPRINT:min:MIN:%5.1lf%sW Min
GPRINT:avg:AVERAGE:%5.1lf%sW Avg
GPRINT:max:MAX:%5.1lf%sW Max
GPRINT:avg:LAST:%5.1lf%sW Last\l
'''

graph_processes = r'''
DEF:running_avg={file}:running:AVERAGE
DEF:running_min={file}:running:MIN
DEF:running_max={file}:running:MAX
DEF:sleeping_avg={file}:sleeping:AVERAGE
DEF:sleeping_min={file}:sleeping:MIN
DEF:sleeping_max={file}:sleeping:MAX
DEF:zombies_avg={file}:zombies:AVERAGE
DEF:zombies_min={file}:zombies:MIN
DEF:zombies_max={file}:zombies:MAX
DEF:stopped_avg={file}:stopped:AVERAGE
DEF:stopped_min={file}:stopped:MIN
DEF:stopped_max={file}:stopped:MAX
DEF:paging_avg={file}:paging:AVERAGE
DEF:paging_min={file}:paging:MIN
DEF:paging_max={file}:paging:MAX
DEF:blocked_avg={file}:blocked:AVERAGE
DEF:blocked_min={file}:blocked:MIN
DEF:blocked_max={file}:blocked:MAX
CDEF:paging_acc=sleeping_avgrunning_avgstopped_avgzombies_avgblocked_avgpaging_avg+++++
CDEF:blocked_acc=sleeping_avgrunning_avgstopped_avgzombies_avgblocked_avg++++
CDEF:zombies_acc=sleeping_avgrunning_avgstopped_avgzombies_avg+++
CDEF:stopped_acc=sleeping_avgrunning_avgstopped_avg++
CDEF:running_acc=sleeping_avgrunning_avg+
CDEF:sleeping_acc=sleeping_avg
AREA:paging_acc#{colors[HalfYellow]}
AREA:blocked_acc#{colors[HalfCyan]}
AREA:zombies_acc#{colors[HalfRed]}
AREA:stopped_acc#{colors[HalfMagenta]}
AREA:running_acc#{colors[HalfGreen]}
AREA:sleeping_acc#{colors[HalfBlue]}
LINE1:paging_acc#{colors[FullYellow]}:Paging
GPRINT:paging_min:MIN:%5.1lf Min
GPRINT:paging_avg:AVERAGE:%5.1lf Average
GPRINT:paging_max:MAX:%5.1lf Max
GPRINT:paging_avg:LAST:%5.1lf Last\l
LINE1:blocked_acc#{colors[FullCyan]}:Blocked
GPRINT:blocked_min:MIN:%5.1lf Min
GPRINT:blocked_avg:AVERAGE:%5.1lf Average
GPRINT:blocked_max:MAX:%5.1lf Max
GPRINT:blocked_avg:LAST:%5.1lf Last\l
LINE1:zombies_acc#{colors[FullRed]}:Zombies
GPRINT:zombies_min:MIN:%5.1lf Min
GPRINT:zombies_avg:AVERAGE:%5.1lf Average
GPRINT:zombies_max:MAX:%5.1lf Max
GPRINT:zombies_avg:LAST:%5.1lf Last\l
LINE1:stopped_acc#{colors[FullMagenta]}:Stopped
GPRINT:stopped_min:MIN:%5.1lf Min
GPRINT:stopped_avg:AVERAGE:%5.1lf Average
GPRINT:stopped_max:MAX:%5.1lf Max
GPRINT:stopped_avg:LAST:%5.1lf Last\l
LINE1:running_acc#{colors[FullGreen]}:Running
GPRINT:running_min:MIN:%5.1lf Min
GPRINT:running_avg:AVERAGE:%5.1lf Average
GPRINT:running_max:MAX:%5.1lf Max
GPRINT:running_avg:LAST:%5.1lf Last\l
LINE1:sleeping_acc#{colors[FullBlue]}:Sleeping
GPRINT:sleeping_min:MIN:%5.1lf Min
GPRINT:sleeping_avg:AVERAGE:%5.1lf Average
GPRINT:sleeping_max:MAX:%5.1lf Max
GPRINT:sleeping_avg:LAST:%5.1lf Last\l
'''

graph_ps_count = r'''
-v
Processes
DEF:procs_avg={file}:processes:AVERAGE
DEF:procs_min={file}:processes:MIN
DEF:procs_max={file}:processes:MAX
DEF:thrds_avg={file}:threads:AVERAGE
DEF:thrds_min={file}:threads:MIN
DEF:thrds_max={file}:threads:MAX
AREA:thrds_avg#{colors[HalfBlue]}
AREA:procs_avg#{colors[HalfRed]}
LINE1:thrds_avg#{colors[FullBlue]}:Threads
GPRINT:thrds_min:MIN:%5.1lf Min
GPRINT:thrds_avg:AVERAGE:%5.1lf Avg
GPRINT:thrds_max:MAX:%5.1lf Max
GPRINT:thrds_avg:LAST:%5.1lf Last\l
LINE1:procs_avg#{colors[FullRed]}:Processes
GPRINT:procs_min:MIN:%5.1lf Min
GPRINT:procs_avg:AVERAGE:%5.1lf Avg
GPRINT:procs_max:MAX:%5.1lf Max
GPRINT:procs_avg:LAST:%5.1lf Last\l
'''

graph_ps_cputime = r'''
-v
Jiffies
DEF:user_avg_raw={file}:user:AVERAGE
DEF:user_min_raw={file}:user:MIN
DEF:user_max_raw={file}:user:MAX
DEF:syst_avg_raw={file}:syst:AVERAGE
DEF:syst_min_raw={file}:syst:MIN
DEF:syst_max_raw={file}:syst:MAX
CDEF:user_avg=user_avg_raw1000000/
CDEF:user_min=user_min_raw1000000/
CDEF:user_max=user_max_raw1000000/
CDEF:syst_avg=syst_avg_raw1000000/
CDEF:syst_min=syst_min_raw1000000/
CDEF:syst_max=syst_max_raw1000000/
CDEF:user_syst=syst_avgUN0syst_avgIFuser_avg+
AREA:user_syst#{colors[HalfBlue]}
AREA:syst_avg#{colors[HalfRed]}
LINE1:user_syst#{colors[FullBlue]}:User
GPRINT:user_min:MIN:%5.1lf%s Min
GPRINT:user_avg:AVERAGE:%5.1lf%s Avg
GPRINT:user_max:MAX:%5.1lf%s Max
GPRINT:user_avg:LAST:%5.1lf%s Last\l
LINE1:syst_avg#{colors[FullRed]}:System
GPRINT:syst_min:MIN:%5.1lf%s Min
GPRINT:syst_avg:AVERAGE:%5.1lf%s Avg
GPRINT:syst_max:MAX:%5.1lf%s Max
GPRINT:syst_avg:LAST:%5.1lf%s Last\l
'''

graph_ps_pagefaults = r'''
-v
Pagefaults/s
DEF:minor_avg={file}:minflt:AVERAGE
DEF:minor_min={file}:minflt:MIN
DEF:minor_max={file}:minflt:MAX
DEF:major_avg={file}:majflt:AVERAGE
DEF:major_min={file}:majflt:MIN
DEF:major_max={file}:majflt:MAX
CDEF:minor_major=major_avgUN0major_avgIFminor_avg+
AREA:minor_major#{colors[HalfBlue]}
AREA:major_avg#{colors[HalfRed]}
LINE1:minor_major#{colors[FullBlue]}:Minor
GPRINT:minor_min:MIN:%5.1lf%s Min
GPRINT:minor_avg:AVERAGE:%5.1lf%s Avg
GPRINT:minor_max:MAX:%5.1lf%s Max
GPRINT:minor_avg:LAST:%5.1lf%s Last\l
LINE1:major_avg#{colors[FullRed]}:Major
GPRINT:major_min:MIN:%5.1lf%s Min
GPRINT:major_avg:AVERAGE:%5.1lf%s Avg
GPRINT:major_max:MAX:%5.1lf%s Max
GPRINT:major_avg:LAST:%5.1lf%s Last\l
'''

graph_ps_rss = r'''
-v
Bytes
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:avg#{colors[HalfBlue]}
LINE1:avg#{colors[FullBlue]}:RSS
GPRINT:min:MIN:%5.1lf%s Min
GPRINT:avg:AVERAGE:%5.1lf%s Avg
GPRINT:max:MAX:%5.1lf%s Max
GPRINT:avg:LAST:%5.1lf%s Last\l
'''

graph_ps_state = r'''
-v
Processes
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Processes
GPRINT:min:MIN:%6.2lf Min
GPRINT:avg:AVERAGE:%6.2lf Avg
GPRINT:max:MAX:%6.2lf Max
GPRINT:avg:LAST:%6.2lf Last\l
'''

graph_signal_noise = r'''
-v
dBm
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Noise
GPRINT:min:MIN:%5.1lf%sdBm Min
GPRINT:avg:AVERAGE:%5.1lf%sdBm Avg
GPRINT:max:MAX:%5.1lf%sdBm Max
GPRINT:avg:LAST:%5.1lf%sdBm Last\l
'''

graph_signal_power = r'''
-v
dBm
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Power
GPRINT:min:MIN:%5.1lf%sdBm Min
GPRINT:avg:AVERAGE:%5.1lf%sdBm Avg
GPRINT:max:MAX:%5.1lf%sdBm Max
GPRINT:avg:LAST:%5.1lf%sdBm Last\l
'''

graph_signal_quality = r'''
-v
%
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Quality
GPRINT:min:MIN:%5.1lf%s%% Min
GPRINT:avg:AVERAGE:%5.1lf%s%% Avg
GPRINT:max:MAX:%5.1lf%s%% Max
GPRINT:avg:LAST:%5.1lf%s%% Last\l
'''

graph_swap = r'''
-v
Bytes' '-b' '1024
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Bytes
GPRINT:min:MIN:%6.2lf%sByte Min
GPRINT:avg:AVERAGE:%6.2lf%sByte Avg
GPRINT:max:MAX:%6.2lf%sByte Max
GPRINT:avg:LAST:%6.2lf%sByte Last\l
'''

graph_old_swap = r'''
DEF:used_avg={file}:used:AVERAGE
DEF:used_min={file}:used:MIN
DEF:used_max={file}:used:MAX
DEF:free_avg={file}:free:AVERAGE
DEF:free_min={file}:free:MIN
DEF:free_max={file}:free:MAX
DEF:cach_avg={file}:cached:AVERAGE
DEF:cach_min={file}:cached:MIN
DEF:cach_max={file}:cached:MAX
DEF:resv_avg={file}:resv:AVERAGE
DEF:resv_min={file}:resv:MIN
DEF:resv_max={file}:resv:MAX
CDEF:cach_avg_notnull=cach_avgUN0cach_avgIF
CDEF:resv_avg_notnull=resv_avgUN0resv_avgIF
CDEF:used_acc=used_avg
CDEF:resv_acc=used_accresv_avg_notnull+
CDEF:cach_acc=resv_acccach_avg_notnull+
CDEF:free_acc=cach_accfree_avg+
AREA:free_acc#{colors[HalfGreen]}
AREA:cach_acc#{colors[HalfBlue]}
AREA:resv_acc#{colors[HalfYellow]}
AREA:used_acc#{colors[HalfRed]}
LINE1:free_acc#{colors[FullGreen]}:Free
GPRINT:free_min:MIN:%5.1lf%s Min
GPRINT:free_avg:AVERAGE:%5.1lf%s Avg
GPRINT:free_max:MAX:%5.1lf%s Max
GPRINT:free_avg:LAST:%5.1lf%s Last\n
LINE1:cach_acc#{colors[FullBlue]}:Cached
GPRINT:cach_min:MIN:%5.1lf%s Min
GPRINT:cach_avg:AVERAGE:%5.1lf%s Avg
GPRINT:cach_max:MAX:%5.1lf%s Max
GPRINT:cach_avg:LAST:%5.1lf%s Last\l
LINE1:resv_acc#{colors[FullYellow]}:Reserved
GPRINT:resv_min:MIN:%5.1lf%s Min
GPRINT:resv_avg:AVERAGE:%5.1lf%s Avg
GPRINT:resv_max:MAX:%5.1lf%s Max
GPRINT:resv_avg:LAST:%5.1lf%s Last\n
LINE1:used_acc#{colors[FullRed]}:Used
GPRINT:used_min:MIN:%5.1lf%s Min
GPRINT:used_avg:AVERAGE:%5.1lf%s Avg
GPRINT:used_max:MAX:%5.1lf%s Max
GPRINT:used_avg:LAST:%5.1lf%s Last\l
'''

graph_tcp_connections = r'''
-v
Connections
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Connections
GPRINT:min:MIN:%4.1lf Min
GPRINT:avg:AVERAGE:%4.1lf Avg
GPRINT:max:MAX:%4.1lf Max
GPRINT:avg:LAST:%4.1lf Last\l
'''

graph_temperature = r'''
-v
Celsius
DEF:temp_avg={file}:value:AVERAGE
DEF:temp_min={file}:value:MIN
DEF:temp_max={file}:value:MAX
CDEF:average=temp_avg0.2*PREVUNtemp_avgPREVIF0.8*+
AREA:temp_max#{colors[HalfRed]}
AREA:temp_min#{colors[Canvas]}
LINE1:temp_avg#{colors[FullRed]}:Temperature
GPRINT:temp_min:MIN:%4.1lf Min
GPRINT:temp_avg:AVERAGE:%4.1lf Avg
GPRINT:temp_max:MAX:%4.1lf Max
GPRINT:temp_avg:LAST:%4.1lf Last\l
'''

graph_timeleft = r'''
-v
Minutes
DEF:avg={file}:timeleft:AVERAGE
DEF:min={file}:timeleft:MIN
DEF:max={file}:timeleft:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Time left [min]
GPRINT:min:MIN:%5.1lf%s Min
GPRINT:avg:AVERAGE:%5.1lf%s Avg
GPRINT:max:MAX:%5.1lf%s Max
GPRINT:avg:LAST:%5.1lf%s Last\l
'''

graph_time_offset = r'''
# NTPd
DEF:s_avg={file}:seconds:AVERAGE
DEF:s_min={file}:seconds:MIN
DEF:s_max={file}:seconds:MAX
AREA:s_max#{colors[HalfBlue]}
AREA:s_min#{colors[Canvas]}
LINE1:s_avg#{colors[FullBlue]}:{inst}
GPRINT:s_min:MIN:%7.3lf%s Min
GPRINT:s_avg:AVERAGE:%7.3lf%s Avg
GPRINT:s_max:MAX:%7.3lf%s Max
GPRINT:s_avg:LAST:%7.3lf%s Last
'''

graph_if_octets = r'''
-v
Bits/s
-l
0
DEF:out_min_raw={file}:tx:MIN
DEF:out_avg_raw={file}:tx:AVERAGE
DEF:out_max_raw={file}:tx:MAX
DEF:inc_min_raw={file}:rx:MIN
DEF:inc_avg_raw={file}:rx:AVERAGE
DEF:inc_max_raw={file}:rx:MAX
CDEF:out_min=out_min_raw8*
CDEF:out_avg=out_avg_raw8*
CDEF:out_max=out_max_raw8*
CDEF:inc_min=inc_min_raw8*
CDEF:inc_avg=inc_avg_raw8*
CDEF:inc_max=inc_max_raw8*
CDEF:overlap=out_avginc_avgGTinc_avgout_avgIF
CDEF:mytime=out_avg_rawTIMETIMEIF
CDEF:sample_len_raw=mytimePREV(mytime)-
CDEF:sample_len=sample_len_rawUN0sample_len_rawIF
CDEF:out_avg_sample=out_avg_rawUN0out_avg_rawIFsample_len*
CDEF:out_avg_sum=PREVUN0PREVIFout_avg_sample+
CDEF:inc_avg_sample=inc_avg_rawUN0inc_avg_rawIFsample_len*
CDEF:inc_avg_sum=PREVUN0PREVIFinc_avg_sample+
AREA:out_avg#{colors[HalfGreen]}
AREA:inc_avg#{colors[HalfBlue]}
AREA:overlap#{colors[HalfBlueGreen]}
LINE1:out_avg#{colors[FullGreen]}:Outgoing
GPRINT:out_avg:AVERAGE:%5.1lf%s Avg
GPRINT:out_max:MAX:%5.1lf%s Max
GPRINT:out_avg:LAST:%5.1lf%s Last
GPRINT:out_avg_sum:LAST:(ca. %5.1lf%sB Total)\l
LINE1:inc_avg#{colors[FullBlue]}:Incoming
#'GPRINT:inc_min:MIN:%5.1lf %s Min'
GPRINT:inc_avg:AVERAGE:%5.1lf%s Avg
GPRINT:inc_max:MAX:%5.1lf%s Max
GPRINT:inc_avg:LAST:%5.1lf%s Last
GPRINT:inc_avg_sum:LAST:(ca. %5.1lf%sB Total)\l
'''

graph_cpufreq = r'''
DEF:cpufreq_avg={file}:value:AVERAGE
DEF:cpufreq_min={file}:value:MIN
DEF:cpufreq_max={file}:value:MAX
AREA:cpufreq_max#{colors[HalfBlue]}
AREA:cpufreq_min#{colors[Canvas]}
LINE1:cpufreq_avg#{colors[FullBlue]}:Frequency
GPRINT:cpufreq_min:MIN:%5.1lf%s Min
GPRINT:cpufreq_avg:AVERAGE:%5.1lf%s Avg
GPRINT:cpufreq_max:MAX:%5.1lf%s Max
GPRINT:cpufreq_avg:LAST:%5.1lf%s Last\l
'''

graph_multimeter = r'''
DEF:multimeter_avg={file}:value:AVERAGE
DEF:multimeter_min={file}:value:MIN
DEF:multimeter_max={file}:value:MAX
AREA:multimeter_max#{colors[HalfBlue]}
AREA:multimeter_min#{colors[Canvas]}
LINE1:multimeter_avg#{colors[FullBlue]}:Multimeter
GPRINT:multimeter_min:MIN:%4.1lf Min
GPRINT:multimeter_avg:AVERAGE:%4.1lf Average
GPRINT:multimeter_max:MAX:%4.1lf Max
GPRINT:multimeter_avg:LAST:%4.1lf Last\l
'''

graph_users = r'''
-v
Users
DEF:users_avg={file}:value:AVERAGE
DEF:users_min={file}:value:MIN
DEF:users_max={file}:value:MAX
AREA:users_max#{colors[HalfBlue]}
AREA:users_min#{colors[Canvas]}
LINE1:users_avg#{colors[FullBlue]}:Users
GPRINT:users_min:MIN:%4.1lf Min
GPRINT:users_avg:AVERAGE:%4.1lf Average
GPRINT:users_max:MAX:%4.1lf Max
GPRINT:users_avg:LAST:%4.1lf Last\l
'''

graph_voltage = r'''
-v
Voltage
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Voltage
GPRINT:min:MIN:%5.1lf%sV Min
GPRINT:avg:AVERAGE:%5.1lf%sV Avg
GPRINT:max:MAX:%5.1lf%sV Max
GPRINT:avg:LAST:%5.1lf%sV Last\l
'''

graph_vs_threads = r'''
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Threads
GPRINT:min:MIN:%5.1lf Min
GPRINT:avg:AVERAGE:%5.1lf Avg.
GPRINT:max:MAX:%5.1lf Max
GPRINT:avg:LAST:%5.1lf Last\l
'''

graph_vs_memory = r'''
-b
1024
-v
Bytes
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:
GPRINT:min:MIN:%5.1lf%sbytes Min
GPRINT:avg:AVERAGE:%5.1lf%sbytes Avg.
GPRINT:max:MAX:%5.1lf%sbytes Max
GPRINT:avg:LAST:%5.1lf%sbytes Last\l
'''

graph_vs_processes = r'''
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Processes
GPRINT:min:MIN:%5.1lf Min
GPRINT:avg:AVERAGE:%5.1lf Avg.
GPRINT:max:MAX:%5.1lf Max
GPRINT:avg:LAST:%5.1lf Last\l
'''

graph_vmpage_number = r'''
-v
Pages
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Number
GPRINT:min:MIN:%4.1lf Min
GPRINT:avg:AVERAGE:%4.1lf Avg
GPRINT:max:MAX:%4.1lf Max
GPRINT:avg:LAST:%4.1lf Last\l
'''

graph_vmpage_faults = r'''
DEF:minf_avg={file}:minflt:AVERAGE
DEF:minf_min={file}:minflt:MIN
DEF:minf_max={file}:minflt:MAX
DEF:majf_avg={file}:majflt:AVERAGE
DEF:majf_min={file}:majflt:MIN
DEF:majf_max={file}:majflt:MAX
CDEF:overlap=majf_avgminf_avgGTminf_avgmajf_avgIF
AREA:majf_avg#{colors[HalfGreen]}
AREA:minf_avg#{colors[HalfBlue]}
AREA:overlap#{colors[HalfBlueGreen]}
LINE1:majf_avg#{colors[FullGreen]}:Major
GPRINT:majf_min:MIN:%5.1lf%s Min
GPRINT:majf_avg:AVERAGE:%5.1lf%s Avg
GPRINT:majf_max:MAX:%5.1lf%s Max
GPRINT:majf_avg:LAST:%5.1lf%s Last\l
LINE1:minf_avg#{colors[FullBlue]}:Minor
GPRINT:minf_min:MIN:%5.1lf%s Min
GPRINT:minf_avg:AVERAGE:%5.1lf%s Avg
GPRINT:minf_max:MAX:%5.1lf%s Max
GPRINT:minf_avg:LAST:%5.1lf%s Last\l
'''

graph_vmpage_io = r'''
DEF:rpag_avg={file}:in:AVERAGE
DEF:rpag_min={file}:in:MIN
DEF:rpag_max={file}:in:MAX
DEF:wpag_avg={file}:out:AVERAGE
DEF:wpag_min={file}:out:MIN
DEF:wpag_max={file}:out:MAX
CDEF:overlap=wpag_avgrpag_avgGTrpag_avgwpag_avgIF
AREA:wpag_avg#{colors[HalfGreen]}
AREA:rpag_avg#{colors[HalfBlue]}
AREA:overlap#{colors[HalfBlueGreen]}
LINE1:wpag_avg#{colors[FullGreen]}:OUT
GPRINT:wpag_min:MIN:%5.1lf%s Min
GPRINT:wpag_avg:AVERAGE:%5.1lf%s Avg
GPRINT:wpag_max:MAX:%5.1lf%s Max
GPRINT:wpag_avg:LAST:%5.1lf%s Last\l
LINE1:rpag_avg#{colors[FullBlue]}:IN
GPRINT:rpag_min:MIN:%5.1lf%s Min
GPRINT:rpag_avg:AVERAGE:%5.1lf%s Avg
GPRINT:rpag_max:MAX:%5.1lf%s Max
GPRINT:rpag_avg:LAST:%5.1lf%s Last\l
'''

graph_vmpage_action = r'''
-v
Pages
DEF:avg={file}:value:AVERAGE
DEF:min={file}:value:MIN
DEF:max={file}:value:MAX
AREA:max#{colors[HalfBlue]}
AREA:min#{colors[Canvas]}
LINE1:avg#{colors[FullBlue]}:Number
GPRINT:min:MIN:%4.1lf Min
GPRINT:avg:AVERAGE:%4.1lf Avg
GPRINT:max:MAX:%4.1lf Max
GPRINT:avg:LAST:%4.1lf Last\l
'''

graph_virt_cpu_total = r'''
-v
Milliseconds
DEF:avg_raw={file}:ns:AVERAGE
DEF:min_raw={file}:ns:MIN
DEF:max_raw={file}:ns:MAX
CDEF:avg=avg_raw1000000/
CDEF:min=min_raw1000000/
CDEF:max=max_raw1000000/
AREA:avg#{colors[HalfBlue]}
LINE1:avg#{colors[FullBlue]}:CPU time
GPRINT:min:MIN:%4.1lf Min
GPRINT:avg:AVERAGE:%4.1lf Avg
GPRINT:max:MAX:%4.1lf Max
GPRINT:avg:LAST:%4.1lf Last\l
'''

stacked_graph_memory = {
    'title': 'memory',
    'number_format': '%5.1lf%s',
    'field_order': ['free', 'cached', 'buffered', 'used'],
    'rrd_args': ['-b', '1024', '-v', 'Bytes'],
    'colors': {
        'free': '00e000',
        'used': 'ff0000',
        'cached': '0000ff',
        'buffered': 'ffb000',
    }
}
