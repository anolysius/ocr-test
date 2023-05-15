name_pattern = r'(?P<title>(Mr|Mrs|Miss|Ms|Dr|Professor|Reverend|Honorable|Captain|Major|Colonel|General)\.?)?(\s+)?' \
               r'(?P<firstname>\w+)\s+' \
               r'(?:(?P<middlename>\w+\.?)\s+)?' \
               r'(?P<lastname>\w+)'

address_pattern = r'(\d+)\s+(.*)+?'

po_box_pattern = r'(.*)O\s[B|b]ox(\s+)?(.*)?'

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA',
          'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
          'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

street = ['Ave', 'Blvd', 'Cir', 'Ct', 'Dr', 'Espln', 'Expy', 'Ext', 'Grn', 'Hwy', 'Ln', 'Pl', 'Pt', 'Rd', 'Rte', 'Sq',
          'Ter', 'Tr']

digit_start_pattern = r'^(\d+).*'

state_start_patter = r'^(AL|AK|AZ|AR|CA|CO|CT|DE|FL|GA|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM' \
                     r'|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY).*'

city_state_zip_pattern = r'(?P<city>(.*)(,)?)\s+' \
                         r'(?P<state>(' \
                         r'AL|AK|AZ|AR|CA|CO|CT|DE|FL|GA|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ' \
                         r'|NM|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY' \
                         r'))\s+' \
                         r'(?P<zip>(\d+))'

street_pattern = r'\b\d+.*?(?:Avenue|Ave|Boulevard|Blvd|Circle|Cir|Court|Ct|Drive|Dr|Esplanade|Espln|Expressway' \
                 r'|Expy|Extension|Ext|Green|Grn|Highway|Hwy|Lane|Ln|Place|Pl|Point|Pt|Plaza|Road|Rd|Route|Rte' \
                 r'|Square|Sq|Terrace|Ter|Trail|Tr|Way|Alley|Arcade|Ascent|Bay|Beach|Bend|Brook|Bypass|Camp|Canyon' \
                 r'|Cape|Causeway|Center|Circle|Cliff|Club|Common|Corner|Course|Court|Cove|Creek|Crossing|Cul|Dale' \
                 r'|Divide|Drive|Estate|Expressway|Extension|Falls|Ferry|Field|Flat|Ford|Forest|Garden|Glen|Green|Grove' \
                 r'|Heights|Highway|Hill|Hollow|Island|Isle|Junction|Key|Knoll|Lake|Landing|Lane|Light|Loaf|Lock|Lodge' \
                 r'|Loop|Mall|Manor|Meadows|Mill|Mission|Mound|Mountain|Neck|Oak|Oasis|Oakland|Orchard|Oval|Park|Parkway' \
                 r'|Pass|Path|Pike|Plaza|Point|Port|Prairie|Radial|Ranch|Rapids|Rest|Ridge|River|Road|Rookery|Run|Shoal' \
                 r'|Shoals|Shore|Shores|Spring|Springs|Square|Station|Stravenue|Stream|Street|Summit|Terrace|Trace|Track' \
                 r'|Trail|Tunnel|Turnpike|Underpass|Union|Upland|Valley|Village|Vista' \
                 r'|Walk|Wall|Way|Well|Wharf|Yard|Encanto|Verde)(_|,|.|;|:)?\b'
