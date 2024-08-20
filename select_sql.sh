#!/bin/bash
# select last modified date diff between en and ja is more than 3 days

sqlite3 summary.db << EOS
select distinct ja.title, en.last_modified, ja.last_modified, (en.lm - ja.lm)/(60*60*24), en.guid from
  (select
     strftime('%s', substr(last_modified, 7, 4) || '-' || 
                    substr(last_modified, 4, 2) || '-' ||
                    substr(last_modified, 1, 2) || ' ' ||
                    substr(last_modified, 12, 2) || ':' ||
                    substr(last_modified, 15, 2) || ':' ||
                    substr(last_modified, 18, 2)) lm, *
   from nsx where language == 'ja') ja,
  (select
     strftime('%s', substr(last_modified, 7, 4) || '-' ||
                    substr(last_modified, 4, 2) || '-' ||
                    substr(last_modified, 1, 2) || ' ' ||
                    substr(last_modified, 12, 2) || ':' ||
                    substr(last_modified, 15, 2) || ':' ||
                    substr(last_modified, 18, 2)) lm, *
   from nsx where language == 'en') en
where ja.guid == en.guid
  and (en.lm - ja.lm)/(60*60*24) > 3;
EOS
