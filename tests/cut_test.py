import re
import unittest
from typing import List

from src.Modules.utils import isCommonForm, isMailForm, extractNames, extractTotalAddress

data = [
    ['Arico Systems, Ltd.', '165 Pinecrest Street', 'Front Royal, VA 22630', 'Tel: 703-229-3130', 'FAX COVER SHEET',
     'To: Pete Flanerty', 'From; Sue Arlco', 'Date:', '4 /i4', '33', "Today'5 farms for NLPC follov.", 'There', 'are3',
     'pages, including this', 'cover sneet', 'Exmail addresses have been updated', 'verified on Constant', 'Contact,'],
    ['Reply to Peter Flaherty', 'Chairman, National Legal and Policy Center', 'From:', 'Mr. Thomas MacKenzie',
     '16635 W. Sheridan Street', 'Goodyear; AZ 85395', 'HJIB',
     'Dear Peter; my 2023 U.S. Congress Directory arrived in good order.', 'To help you fight corruption;',
     'am enclosing', 'tax-deductible gift of:', 'Ds1OO  DS150', 'Ds200', 'Ds250', 'Dssoo', 'DS1,000', 'Ds', 'other',
     'Please make your check payable to:', '"Natlonal Legal and Policy Center\'', 'NLPC"',
     'want t0 make a single gift today using my credit card. Please make', 'one-time charge to my credit card of $',
     'Lco2', 'Mastorcard', 'Discover DAMEX', 'Card number', '54el3%4', '4', '45', 'Expiration date', '221',
     'Cardholder Signature_', 'ZLeal', 'sMkke', 'want to enroll in the Monthly Gift', 'Program: Please make a charge',
     'to my credit card of $', 'each month:', 'understand that', 'may', 'cancel al any time.', 'Visa', 'Mastercard',
     '0 Discover', 'AMEX', 'Card number', 'Expiration date', 'Cardholder Signature_', 'NLPC Tarpayer ID #52-1750188',
     '107 Park WasMington Court', 'Falls Church; VA', '22040', '703-237-1970', 'fax 703-297-2090',
     'e-mail: pflaherty @nlpc org', 'Wt nIpc org', 'Visa'],
    ['Reply to Peter Flaherty', 'Chairman; Natlonal Legal and Policy Center', 'From:', 'Mr . David N. Grandon',
     '91 Poplar Ave', 'New Cumberland, PA   17070', 'HJIC', '0Dear Peter', 'my',
     '2023 U.S. Congress Directory arrived in good order.', 'To help you fight corruption',
     'am enclosing a tax-deductible gift of:', 'DS1OO', 'DS15o DS200', 'Ds250', 'Dssoo', 'DS1,000', 'DS', 'other',
     'Please make your check payable to:', '"National Legal and Policy Center\'', 'or "NLPC"',
     'want to make a single gift today', 'my credit card. Please make', 'one-time charge to my credit card of $',
     'DVisa', 'C Mastercard @ Discover', 'KamEX', 'Card number', '3712', '35477-7309', 'Expiration date', '/25',
     'Cardholder Signature', 'want t0 enroll in the Monthly Gift Program', 'Please make a charge',
     'to my credit card of $', 'each month:', 'understand that', 'may', 'cancel at any time',
     'Vlsa D ivasiuiald &ciscovei', 'C AMcX', 'Card nuntber', 'Expiration date', 'Cardholder Signature',
     'NLPC Taxpayer ID #52-1750188', '107 Park Washington Court=', 'Falls Cnurch', '22046', '703-237-1970',
     'fax 703-23142090', 'e-mail: pllaherty @nlpc org', 'Www nIpc Org', 'using'],
    ['Reply to Peter Flaherty', 'Chairman; Natlonal Legal and Pollcy Center', 'From:', 'Mr. Juan Y. Forster',
     '18971 Newton Ave:', 'Santa Ana; CA 92705', 'H3IB',
     'EDear Peter, my 2023 U.S. Congress Directory arrived in good order.', 'To help you fight corruption,', 'am',
     'enclosing', 'tax-deductible giit of:', 'Ps100', 'DS150', 'DS200', 'Ds250', 'Dssoo', 'DS1,000', 'Ds_', 'other',
     'Please make your check payable to:', '"National Legal and Policy Center" or', 'NLPC"',
     'want to make a single gift today using my credit card. Please make', 'one-time charge to my credit card of $_',
     'Visa', '0 Mastercard', 'Discover D AMEX', 'Card number', 'Expiration date', 'Cardholder Signature',
     'want to enroll in the Monthly Gift Program. Please make', 'charge', 'to my credit card of $_', 'each month:',
     'understand that', 'may', 'cancel at any time_', 'Visa', 'Mastercard', 'Discover 0 AMEX',
     'Cash Management Account"', '5502', 'JuanyForster Wtee', 'WAI', 'carolymifonstea TtEL', '12471Enc', '%s-201 _',
     'Jzns7ual', 'Rayto the', 'ItAMucl:', '2da', 'I08. @', 'Order ol _', 'Dollars', '@ne Zun', 'Nn', 'nlpc org',
     'MERRILLES', 'Lanotahitich (Omea#', 'For', '408430*?E ?0', '041182527*9125502', 'vo [oe'],
    ['Reply to Peter Flaherty', 'Chairman; National Legal and Policy Center', 'From:', 'Elizabeth Courtney',
     '1152 Via Verde', '#110', 'San Dimas', 'CA 91773-4401', 'HJIB', 'Peter, my 2023 U', 'To help you fight corruf',
     'MS100', 'DS150', 'Ds200', '8', 'Aedmeb nL', '1', 'Us', '2x7', 'Uhau#', 'UuDLdnz', 'Fqeubbcen', 'TLL',
     'Lineep-Loho__83', '0', 'endbsues ZL', '72', '4LA', 'Eiutoy', '1', 'ArU', '1', '0L', 'Sdorrru €eeh', 'I', 'H', '',
     'ueuahu', 'Ii', 'Elalc', ':', '702', 'Dear', "'sti", 'DDexeu_', 'ulLlunah UTD', 'Umeu', 'Zozz', 'S', 'Ll4eLr',
     'Iashspall;', '8', '1', '1', 'Co'],
    ['Andrer', 'Sabin', 'Horld', 'Trade', 'GoM', '700', '250 Greenvich', 'st .', 'ste', '4620', 'New York , NY',
     '10007', '003%;XtY', 'Peter Flaherty', 'GoaiTTAD', 'Natlonal', 'Legal', 'and Policy Center', 'PO Box 486',
     'Front Royal', '22630-0010', '22630-00ioas', 'mlpepnV"pmllVlsllmlhulollelwm:', '7 85', 'HSBC', 'ANDREW SABIN',
     '4-104/?10', 'DAXER &e', 'MnINAL bretl', 'tur', 'rwe', '7s4', 'DOLLAI', 'CZJ', 'Nht', 'Juieonnana', '6p7e MRE.',
     '#*0', '78 5 24"', '40210010884', "4340377567'", 'ANDAEW S4BIN', '1785', '6 8uy'],
    ['Reply to Peter Flaherty', 'Chairman, National Legal and Policy Center', 'From:', 'Mr. John W: Pennisten',
     '135 Willow Street_', '#711', 'Brooklyn, NY 11201', 'H3IB',
     'Dear Peter, my 2023 U.S. Congress Directory arrived in good order:', 'To help you fight corruption;',
     'am enclosing a tax-deductible gift of:', '@S1OO) DS150', 'Dsz00', 'DS250', 'Ds5oo', 'DS1,000', 'Ds', 'other',
     'Please make your check payable to:', 'Natlonal Legal and Pollcy Center" or "NLPC"',
     'want to make a single gift today using my credit', 'Please make', 'one-time charge to my credit card of $_',
     'Visa', 'Mastercard', '0 Discover', 'AMEX', 'Card number', 'Expiration date', 'Cardholder Signature',
     'want to enroll in the Monthly Gift Program: Please make a charge', 't0 my credit card of $', 'each month_',
     'understand that', 'may', 'cancel at any time:', '2423', 'JOHN W: PENNISTEN', 'TllorsT', 'T FM', 'DROORTN Ni',
     '1iz01', '021i 4A233', '0', 'ZteplnABhetaez $ [0of', 'E1', 'Aer', '"oe', 'A', 'CHASEO', 'Onb', 'nipc Org', "7t'",
     '#0', "'ooo0", '260031303/2423', 'card:', '95onu', 'E2_'],
    ['Reply to Peter Flaherty', 'Chairman; National Legal and Policy Center', 'From:', 'Dr. Ronald Komich',
     '4002 Brambletye Court', 'Greensboro, NC 27407', 'HJIB', 'Dear Peter, my 2023 U.S.',
     'Congress Directory arrived in good order:', 'To help you fight corruption,',
     'am enclosing a tax-deductible gift of:', 'DS100', 'DS150', 'Ds200', 'Ds250', 'Dssoo', 'DS1,000', 'Ds', 'other',
     'Please make your check payable to:', '"National Legal and Pollcy Center" or "NLPC"',
     'want to make a single gift today using my credit card. Please make', 'pne-lime charge to my credit card of $_',
     'Visa', 'Mastercarc', '0 Discover', 'DAMEX -', 'Expiration date', 'Card number', 'Cardholdor Signature',
     'want to enroll in the Monthly Gift Program; Please make', 'charge', 'credit card of $', 'each month:',
     'understand that', 'may', 'to my', 'cancel at any time.', 'Jotorcargi', 'NDiscovor 0 AMEX', '001875', 'stoMrd',
     'Kroigich', 'Gcri', '40ne Wchmarean', 'Cransborj', '6c7747 7771', 'DATE', 'A', 'Lols', 'Dhone', 'Nt) Ge', 'Ct',
     '00,', 'S <', 'LiLu', 'DOLLAn?', '101}', '0 _A', '"00.8?54\'', '"053104121413400045093801"', 'P,y'],
    ['Reply to Peter Flaherty', 'Chalrman, National Legal and Pollcy Center', 'From:', 'Mr. David Larsen',
     '1673 De Anza Blvd', 'San Mateo, CA 94403', 'P23285', 'Peter; my 2023 U.S. Congress Directory arrived in good',
     'order. To help you fight Biden', 'his allies', 'am enclosing', 'tax-deductible gift of:', 'Ds5o0', 'DS1,000',
     'Ds2,500', 'Ds5,000', 'DS10,000', '>', 'other', 'Visa', 'Mastercard 0 Discover D AMEX', 'Please bill my credit',
     'Expiration date', 'Cerd number', 'Cardholder Signature_', 'Please make your check payable to:',
     '"National Legal and Policy Center"', 'Or "NLPC"', 'Please fold and return this reply along with', 'check',
     'in the envelope provided:', 'M-AT /', 'DAVID LARSEN', '614', 'lity account', 'BamVateO Ca 0440I 3952',
     '4/14/2023', 'National Legal', 'Poliinn Ordor 0', 'and', 'Policy', 'Center', '#0o', '0o#', '0188', 'hundred',
     'andno/10O*tot*tetttotttotttttttt', 'upali', '2046', 'citibank"', 'MwW,nlpcorg', 'CIMaNaNa', 'JEms', '032074844',
     'Loo', '767706 ?0*', '06 +4', '(Dear', 'and', 'card', 'your', 'Ona'],
    ['Reply to Peter Flaherty', 'Chairman, National Legal', 'Policy Center', 'From:', 'Mr. Richard', 'Lohr',
     '25500 Adams Rd.', 'Los Gatos, CA 95033', 'H31B',
     'Dear Peter, my 2023 U.S. Congress Directory arrived in good order.', 'To help you tight corruption,',
     'am enclosing', 'tax-deductible gift of:', 'DS1OO', '4s15o Dszoo 0S250', 'Dssoo', 'OS1,000', 'DS', 'other',
     'Please make your check payable t0:', '"National Legal and Policy Center\'', 'Or "NLPC"',
     'want to make a single gift today using my credit card:', 'Please make', 'one_time charge t0 my credit card of $',
     'Visa', '0 Mastercard', '0 Discover 0 AMEX', 'Card number', 'Explration date', 'Cardholder Signature_',
     'want to enroll in the Monthly Gift Program: Please make', 'charge', 'to my credit card of $', 'each month_',
     'understand that | may', 'cancel at any time_', '1401', 'Elteni', 'RICHARD ', 'LOHR', 'E3a5', 'AeTI-Calr',
     '2/2/23', '#Met_Eeeee_DE et', '$ /50', '4no', 'Dmedn4 24e4 +', '777ed', 'EANKaWEST', 'L', 'nnlpc org', '02',
     '100?8 2:', '0090363277', '01404', 'and', 'LE'],
    ['Reply to Peter Flaherty', 'Chairman; National Legal and Policy Center', 'From:', 'Mr. Mark S', 'Funk',
     'PO Box 2479', 'Gardnerville, NV 89410', 'H3IA',
     'Dear Peter, my 2023 U.S. Congress Directory arrived in good order.', 'To help you fight corruption,',
     'am enclosing a tax-deductible gift of:', 'Essoo OS1,000', "Dsz,500' Css,ouo OS1O,000", 'DS_', 'other',
     'Please make your check payable to:', '"National Legal and Policy Center" or', 'NLPC"',
     'want to make a single gift today using my credit card. Please make', 'one-time', 'charge to my credit card of $_',
     'Visa', '0 Mastercard', 'Discover D AMEX', 'Card number', 'Expiration date', 'Cardholder Signature',
     'want to enroll in the Monthly Gift Program: Please make', 'charge', 'to my credit', 'of $_', 'each month_',
     'understand that', 'may', 'cancel at any time_', 'X-etini', 'MaRK Funk Or', '2834', 'SherrY FUNK', 'FCBOX 7413',
     'Onetea nlle', 'acio  4a', 'Alzlzz', '347.88Fe', 'MLPc', '50a', '04', 'Lamt', '@Sbank', 'unlpc,org', '02',
     '20+6944', '153?9534 L00""2834', 'card'],
    ['Reply to Peter Flaherty', 'Chairman; National Legal and Policy Center', 'From:', 'Mrs_', 'Florence Speck',
     'PO Box 222016', 'Carmel, CA 93922', 'HJIB', 'Dear Peter; my 2023 U.S. Congress Directory arrived in good order:',
     'To help you fight corruption,', 'am', 'enclosing a tax-deductible gift of:', 'DS1OO DS150', 'Dsz00  Ds250',
     'Dssoo', 'DS1,000', 'DS', 'other', 'Please make your check payable to:',
     '"National Legal and Policy Center" or "NLPC"',
     'want t0 make a single gift today using my credit card. Please make', 'one-time charge to my credit card of $_',
     'Visa D Mastercard', 'ODiscover 0AMEX', 'Card number', 'Expiration date', 'Cardholder Signature',
     'want to enrollin the Monthly Gift Program_', 'Please make a charge', 'to my credit card of $', 'each month:',
     'understand that', 'may', 'cancel at any time', 'Visa', '0 Mastercard', 'Discover DAMEX', '1599',
     'FLORENCE SPEcKs 0877', '052', '00X 12201', '0J1-076', 'CAAMEL', 'canz -dic', '4212', 'DO', '3769', 'Dollalt',
     'Unzuane', '4111)', 'Vw nlpc org', 'Goldenl', 'goldenLcom', '"21.75261', 'Do00ze"', "2377'", '1599', 'LLPc'],
    ['Reply to Peter Flaherty', 'Chalrman', 'National Legal and Pollcy Center', 'From:', 'Phyllis Johnson',
     '6615 N. Smoke Tree Ln', 'Paradise Vly, AZ 85253', 'P23285',
     'Dear Peter, my 2023 U.S: Congress Directory arrived in good', 'order: To help you tight Biden', 'his allies;',
     'am enclosing', 'tax-deductible gift of:', 'Dssoo', 'DS1,000   0S2,500', 'Ds5,00o', 'DS10,000"', 'S5 04', 'other',
     'lease bill my credit card', '0 Visa', '0 Mastercard 0 Discover', 'AMEX', 'Card number', 'Expiration date',
     'Cardholder Signature', 'Please make your check payable to:', '"National Legal and Policy Center" or "NLPC"',
     'Please fold and retum', 'reply along with', 'check', 'Ine enveiope', 'proviaed.', 'PHYLLIS', 'JOHNSON', '3422',
     'account', 'DARADGE', '3253', '4-3-22', 'c#ecr "ue', 'Patote', 'NLPc', '550', '4 + ~Ln', '046', 'wnipc org',
     'FirstCitizEns Bank', 'Cllle | Axuaa', '{22.8733500092600202950', '03422', 'and', 'this{', 'your'],
    ['Gregory', 'Casgady', 'NORTH TEXAS IX PRDC', '4184', 'Hal Lnont Dr', 'DALLASTX 750', 'Grapevine,', '76051',
     '15 APR 2023', 'PM G', '44', 'Peter Flaherty', 'naiti', 'National Legal', 'and', 'Policy', 'Center', 'PO Box',
     '486', 'Front Royal ,', '22630-', '0010', '22830-0010e6', 'u"linUln\' h" Iohu ivll wwlilh"pillai\'jnjji', 'Ja-arn',
     'GreGORY ALLAN CASSADY', 'JEAN', 'CASSADY', '"1h', 'Oart?_', 'VZ Pe', '$ 50.', 'FiFzz', '22', 'Zo', 'DolLARS',
     'JRMorgan', 'JPPORAN@-UGLENKRA', 'Zun', '26 7084134', '75864\'0Li"*?27', '1727'],
    ['Reply to Peter Flaherty', 'Chalrman, National Legal and Policy Center', 'From:', 'Mrs. Kathy Crow',
     '4700 Preston Road', 'Dallas, TX 75205-3712', 'H3TA',
     'DDear Peter, my 2023 U.S. Congress Directory arrived in good order:', 'To help you fight corruption,',
     'am enclosing a tax-deductible gift of:', 'Xeecc', 'Ce;,occ DCz,500', 'Cse,ooo DS10,n00', 'Ds', 'other',
     'Please make your check payable to:', '"National Legal', 'Policy Center"', 'NLPC"',
     'want to make a single gift today using my credit', 'Please make', 'one-time charge to my credit card of $',
     'Visa D Mastercard', 'Discover', 'AMEX', 'Card number_', 'Expiration date', 'Cardholder Signature_',
     'want to enroll in the Monthly Gift Program: Please make a charge', 'to my credit card of $', 'each month:',
     'understand that', 'may', 'cancel at anv time:', 'Visa', 'D Mastercard', '0 Discover', 'DAMEX', '30nte', '16165',
     'Hanlin', 'Or KATHERINE RAYMOND Crow', '#toD prestonad:', '@ALlise-45', '4-13-23', 'Ew884Kiaticxa | legal and',
     'Ceniter', '50.00', 'Xx', 'Fiv hurdxd', 'OLlzs', 'NOrTHERYTRJST ANChCA ACCOUNT', 'w.nlpc org', 'Northern Trust',
     'Mirouillun iilce Cdlant', 'Contribu-tib', '0o 6O64I;', 'oooioioo4or /6165', 'TmtceteAueert', 'So eno', 'and',
     'card,', 'Palicy'],
    ['Reply to Peter Flaherty', 'Chairman', 'National Legal', 'and Policy Center', '+h2', 'From:',
     'Mr. & Mrs. Leon & Judith Drone', 'It', '25 Lancaster Court', 'do', 'New Providence, NJ 07974', 'HJIB',
     'Dear Peter, my 2023 U.S. Congress Directory arrived in good order;', 'To help you fight corruption,', 'am',
     'enclosing a tax-deductible giit of:', 'Ds1o_DS150', '0S2O0', 'Ds250', 'Ossoo', 'DS1,000', 'DS', 'other',
     'Please make your check payable to:', '"National Legal and Policy Center" or "NLPC"',
     'want to make a single gift today using my credit card: Please make', 'pne-time charge to my credit card of $_',
     'Visa D Mastercard', 'D Discover D AMEX', 'Expiration date', 'Card number', 'Cardholder Signature',
     'want to enroll in the Monthly Gift Program: Please make', 'charge', 'to my credit card of $', 'each month:',
     'understand that', 'may', 'cancel at any time:', 'HOc', '@iccolen', 'MLAMMFX', 'LeON', 'DAOHE', '5587', 'DRONE',
     'Wnrdn', 'Mfcnaman', 'NELFA DATDIEAA DTAYAIAIA', '0+ZJ3', 'ardl', 'Yo The', 'NatienaL', 'Cealer=', '$ Jou',
     'Huadred', 'Loc', 'peALefh', 'BANK OfAMERicA', 'pc org', 'ACaT3d', 'GHI', '#0212003394', '004080505', '197*556 ?',
     't04', 'Thank', 'diveco(-', 'help Pul .', 'Ju', 'Ljca', 'Nudith', 'Peli/', 'Lei'],
    ['Reply to Peter Flaherty', 'Chalrman; National Legae', 'and Policy Center', 'From:', 'Mr. Larry Lewis',
     '604 Northlake Ave', 'Ridgeland; MS 39157', 'P23286',
     'Dear Peter, my 2023 U.S. Congress Directory arrived in good', 'order: To help you fight Biden and his allies;',
     'am enclosing', 'tax-deductible gift of:', 'Dssoo', 'Ds:,00o', 'Ds2,500', 'Ds5,000', 'Ds10,000', 'other', 'card',
     'Visa', 'Mastercard D Discover D AMEX', 'Please bill my credit', 'Expiration date', 'Card number', 'PL 86834329',
     'L12', '0)', 'L86831329 [', 'mL', 'iccount', '42268518 G', '10', 'Lnlpc org', '72i22605180', '10'],
    ['Reply to Peter Flaherty', 'Chairman, National Legal and Policy Center', 'From:', 'Mr. Robert C . Bergey',
     '2120 Mixsell Ave', 'Bethlehem, PA  18015', 'H3IB',
     'Dear Peter, my 2023 U.S. Congress Directory arrived in good order:', 'To help you fight corruption,',
     'am enclosing a tax-deductible giit of:', 'ESio OSis0', 'Dsz00', 'Dsz5u', 'DssOO', 'OS1,O0O', 'other',
     'Please make your check payable to:', '"National Legal and Policy Center" or "NLPC"',
     'want to make a single gift today using my credit card. Please make', 'a one-time',
     'charge to my credit card of $_', 'Visa', 'D Mastercard', '0 Discover', 'D AMEX', 'Card number', 'Expiration date',
     'Cardholder Signature', 'want to enroll in the', 'Monthly Gift Program:', 'Please make a charge',
     'to my credit card of $_', 'each month:', 'understand that', 'may', 'cancel at any time', 'ROBERT', 'BERGEY',
     '1686', 'DARY JANE', 'beRGEY', 'nee', 'Mrdamaek', 'BETHLEMDAPA1r016', 'o//22', '58', '$ /00.', 'LEZeNZJ', '3/2o',
     'pDullzn', 'Bank', "'nlpc org", "Uuu Catn=Iant'", '"03600+8084:', '3 ? 293186 S', '1686', 'topzzrt'],
    ['Ben janin', 'Hard', 'OAKLAND CA', '945', '1420', 'California', 'stroet', 'Berkeley ,', '94703', '14 APR 2023',
     'PM 3', 'Poter Flaherty', 'Chairman', 'National Legal', 'and Policy Center', 'PO Box 406', 'Front', 'Royal',
     '22630-0010', '22630-001o36', 'piijjuiplejejep Ieniiphiipep lpsi jviluj Vlkyl', '6221', 'BENJAMIN WARD',
     '4191210 4 3', 'Trudy Keh', 'ET-WARD', '4Ll', '730 tnE', 'NaLi', 'LezLLPakssL_  $ ) 6v', 'Curr 0l', '01', '1iid',
     'fnli', 'mre-LL', '021042882 0125663591*', '06 22 4', '3013'],
    ['Reply to Peter Flaherty', 'Chairman, National Legal and Policy Center', 'From:', 'Mr . Michael J', 'Mahoney',
     '177 Alsace Street', 'Bridgeport, CT  06604', 'HZOA', 'MDear Peter;', 'we must fight and defeat Liberal double',
     "standards in 2023. To keep NLPC's momentum going in", 'this critical year,',
     'am enclosing a tax-deductible gift of:', 'Dssoo', 'DS1,000', 'Ds2,500', 'Ds5,000', 'DS10,000', '2 $', 'other',
     'D Please bill my credit card', 'Visa 0 Mastercard', 'Discover D AMEX', 'Card number_', 'Expiration date',
     'CApnerar', 'L { -', 'Cardholder Signature', 'want t0 receive occasional',
     'Email bulletins ad updates on NLPC projects_', 'E-mail address', '5858', 'MICHAEL', 'MAHONEY', 'Ai', 'AEAA',
     '4.(7 -', 'J037', 'BRIDEEPORT CI 0+604-5215', 'To Mle', 'L?e', "52'", 'UC', 'PLeo', 'FiFtt', '440', 'Jly)', 'E',
     'Fidelity', 'paper', 'Of AMERICA', "AcHE UItem'", 'InL', 'bahr=', '#D', '19005714: 009393888906"5858', '#nlpc.org',
     'BANK'],
    ['Reply to Peter Flaherty', 'Chairman; National Legal', 'and', 'Policy Center', 'From:', 'Leezy Sculley',
     '21 John Street', 'Greenwich', 'CT 06831', 'P2jt85', 'Dear Peter, my 2023 U.S: Congress Directory arrived in good',
     'order: To help you fight Biden and his allies;', 'am enclosing a', 'tax', '~deductible gift of:', 'G3500',
     'DS1,000', 'DS2,500', 'Ds5,000', 'DS10,000', 'other', 'Please bill my credit card',
     'D Visa D Mastercard 0 Discover D AMEX', 'Card number', 'Expiration date', 'Cardholder', 'Signature_',
     'Please make your check', 'to:', '"\'National Legal and Policy Center" or "NLPC"', '4407', 'Lee SCULLEY', 'HZLD',
     'HL? !', 'account', 'Muttsalsqakod Bsfetal', 'S1D', '76', '7e0_', 'BOL4', 'Fuz hun', 'CHASEO', '046', 'W,nlpc.org',
     'amatimn', '40', 'looo', '2362834*4402', 'payable', 'cuer*', 'ELLO;'],
    ['Reply to Peter Flaherty', 'Chairman; National Legal', 'Policy Center', 'From:', 'Mrs. Carol Petrillo',
     '3 Carol Lane', 'Mamaroneck; NY 10543', 'HJIG', 'Dear Peter, my 2023', 'Congress Directory arrived in good order:',
     'To help you fight corruption;', 'am enclosing a tax-deductible gift of:', 'DS1O0', 'Ds15o', 'Ds200', 'DS250',
     'Dssoo', 'DS1,000', 'DS', 'other', 'Please make vour check navahleto', 'Kd Olm', 'No Il', 'Dorcl', 'Lcdui',
     '24358', 'CAROL ANN PETRILLO', 'FELIX MPETRILLO,JR;', 'CAAOL DU', '42023', 'MMARONECK, Hy 10541', '150.00',
     'Rayto"', '84089 38', 'NATIONAL', 'EGAL AND POUCY CENTER', 'Hundred Fiflty and 0W', '00"*"', 'MOILAAS', 'NATIONAE',
     'LEGAEAND POLICY CENTER', '107 PARK WASHINGTONCOURT', 'FALLS CHURCH VA 22028', 'VENC', 'UlzHz', '"0263500 #0',
     '1000024', '786 */97687', '24358', 'CAROL AnN PEIRILLO', 'PETRILLO, JR;', "4'142023",
     'NATIONAL LEGAL AND Policy CENTEA', 'Discovni', 'Paxmort', 'Dale', 'Type', 'Reference', 'Original Amt',
     'Balance Due', '150.00', '150.00', '150.00', '4142023', 'Check Amount', '450-vC', '150,00', 'U.S', 'Feld *'],
    ['Reply to Peter Flaherty', 'Chairman', 'National Legal and Policy Center', 'From:', 'Judith C', 'Beeler',
     '1257 Stallion St', 'Ranson; WV 25438', 'H3IA',
     'DDear Peter, my 2023 U.S. Congress Directory arrived in good order.', 'To help you fight corruption;',
     'am enclosing a tax-deductible gift of:', 'Essoo OS1,00o', 'DSz,s00  OS5,000 DSto,00o', 'D5', 'cther',
     'Please make your check payable to:', '"National Legal and Policy Center\'', 'NLPC"', 'want to make a single gitt',
     'using my credit card. Please make', 'one-time charge to my credit card of $', 'Vise', 'Judidh €', 'Card r',
     'LEE E RODRIGUEZ', '3553', '1257 STALLON ST', 'MEIhzaai', 'RansouIv ?7n6772', 'Lpr 23', 'Cardh', 'B7tNLPc', '5oo',
     'wal', 'fvaL6a', 'Wsa', 't0 m', 'Dulr', 'canc', '5S', 'USAA', '35753805', '0 Vis', 'hut hb', '40242E 94',
     '4o3W35/50', '3553', 'Card', 'Cardholder Signature', 'NLPC Taxpayer ID #52-1750188', '107 Park Washington Court',
     'Falls Church; VA', '22046', '703-237-1970', 'fax 703-237-2090', 'e-mail: pilaherty@nlpcorg', 'Wawnipc org', 'te',
     'F', 'hu 4 4 h #Ltz', 'mplk tLtail', 'Datzaz', 'er', '{z', 'Tl', 'Mtst', 'i', '(tan^', '4', 'a+n', '63', '(40 & 7',
     '{today', 'BEELER', '~4 -'],
    ['Reply to Peter Flaherty', 'Chairman, National Legal and Policy Center', 'From:', 'Mrs. Gesine K: Abrutyn',
     '125 Westminster Dr;', 'Dover; DE', '19904', 'H29E', 'QDear Peter,', 'we must fight and defeat Liberal double',
     "standards in 2023. To keep NLPC's momentum going in", 'this critical year,', 'am', 'enclosing',
     'tax-deductible gift of:', 'Ls5o', 'DS75', 'DS10O', 'DS150', 'Ds200', 'Ds250', 'other',
     'D Please biIl my credit card', 'D Visa', '0 Mastercard', 'Discover 0 AMEX', 'Card number', 'Expiration date_',
     'Cardholder Signature', 'want', 'receive occasional E-mail bulletins and updates on NLPC projects.',
     'E-mall address', '1705', '\'C"', 'GESINE [', 'ABRUTYN', 'JsteADH', 'DOVEA; DE', 'Xl623', '188', 'a#ALfc',
     'Fidelity', 'suedkioe', 'DOLLARS', 'MTBark', '046', 'Wnlpc org', 'Mela', 'duuls', '403*3029550', '98683.34737',
     '705'],
    ['Reply to Peter Flaherty', 'Chairman', 'National Legal and Pollcy Center', 'From:', 'Mr . Donovan Heckman',
     'PO Box 87', 'White Bird, ID 83554', 'HJIc', 'Dear Peter; my 2023 U.S. Congress Directory arrived in', 'order.',
     'To help you fight corruption,', 'am enclosing a tax-deductible gift 0t,', 'Ds1o DS15O', 'Dsz00', 'Ds250', 'Dssoo',
     'DS1,000', 'Ds', 'other', 'Please make your check payable to:', '"National Legal and Policy Center" or "NLPC"',
     'want to make a single gift today using my credit card: Please make', 'one-time charge to my credit card of $',
     'Visa D#astercerd', 'D Dicccver 0 AMEX', 'Expiration date', 'Card number', 'Cardholder Signature',
     'want to enroll in the Monthly Gift Program: Please make a charge', 'to my credit card of $', 'each month:',
     'understand that', 'may', 'cancel at any time_', 'Tecln', '12756', '8. HECKMAN', '07.H411 17oe', 'isilnsn',
     '4-13-22', ' [', 'FbIng', 'NLP', '4A', 'unlpc org', '"26103799 0201051718', '12756', 'good', '96', '[71'],
    ['Reply to Peter Flaherty', 'Chairman, National', 'Legal and Policy Center', 'From:', 'Mrs. Ann Good',
     '5522 Homeville Rd:', 'Oxford, PA 19363', 'HJIB',
     'Dear Peter;, my 2023 U.S. Congress Directory arrived in good order:', 'To help you fight corruption;',
     'am enclosing a tax-deductible gift of:', 'Ps10 DS150', 'Ds2o0 Ds250', 'Dssoo', 'DS1,000', 'DS_', 'other',
     'Please make your check payable to:', '"National Legal and Policy Center" or "NLPC"',
     'want to make a single gift today using my credit', 'Please make', 'gne-time charge to my credit card of $_',
     'Visa', 'D Mastercara', '0 Discover', 'DAMEX', 'Expiration date', 'Card number', 'Cardholder Signature',
     'want to enroll in the Monthly Gift Program:', 'Please make a charge', 'to my credit card of $', 'each month',
     'understand that', 'may', 'cancel at any time_', 'Visa', 'Mastercard', 'Discover @ AMEX', 'ANN GOOD', '14633',
     'ROBERT GOOD', '-52065', 'RO-D', 'L0 Apr 2023', 'Ool)', 'Mtbr?ue National] Eqqland', 'Ceaterj $ Ioo.o', 'Jun dud',
     'ad', 'noln', 'unlpc org', 'FIRETIGHTT? AND RESCLE TEC -YICIAN', 'SANTANDER BaNK; MA_', 'HF4O', 'Ondien 2ozz',
     'Hovb', '"2313726984', '538105522674633', 'card,', 'Policy', 'Yyioo', 'O'],
    ['Reply to Peter Flaherty', 'Chairman; National Legal', 'and Policy Center', 'From:', 'Mr. David Davies',
     '1835 N. Highway AIA Apt: 503', 'Indialantic, FL 32903', 'P23285',
     'Dear Peter, my 2023 U.S: Congress Directory arrived in good', 'order. To help you fight Biden and his allies,',
     'am enclosing', 'tax-deductible gift of:', 'Ds5jo', 'Dst,oo0', '052,500', 'Ds5,000', 'DS10,000', 'Jov', 'other',
     'Please bill my credit card', '0 Visa', '0 Mastercard', 'Discover D AMEX', 'Card number', 'Expiration date',
     'Cardholder Signature', 'Please make your check', 'to:', '"National Legal and Policy Center"', 'or "NLPC"',
     'Please fold End return thle reply elong with your check', 'in the envelope provided,', 'David', 'WDAVIES', '3439',
     'CONNIE [', 'DAMIES', '#atulrtt', 'account', 'lmATni', 'PAIHTED POST M1670', '4_Ly-25', 'aethon', 'Oder', 'NLPc',
     '$ /60', '188', 'Clle', 'sud OLS)', 'Lour', '2046', 'FBTAGE', 'Vanlpc org', '"22238 #88 2415070003 20908303439',
     'payable'],
    ['Terrell B.', 'pounds', 'ORLANDO FL', '328', '1550 Peningula Dr', 'Tavares', '32778', '15 APR Zuzi', 'PM 2',
     'Peter', 'Flaherty', 'Chairian', 'National', 'Legal', 'and', 'Polloy', 'Center', 'Bor]406', 'Front Roxal',
     '22630-0010', '22630-0oiobs', 'I[Vur"" Whbh[Vt"tr | Ulluutu pe] lmliveH', 'Land of the Free', '1247', 'TERREU',
     'MOHADS', 'Because of the Brave', 'TFmkR', '#OLIE', '41112', 'Fahta', '02', 'Or &', '[YcLieda_Leqer Ureliq',
     'Cets SxX', 'LE', 'Dellaz', '4lyanz', 'ILTHUII', 'Es-d', 'Zenele', ":063402152/1000094380200'", '1247'],
    ['Reply to Peter Flaherty', 'Chairman, National Legal and Policy Center', 'From:', 'Mr. J_', 'Bradner Smith',
     '1819 Hunter Lane', 'Saint Paul, MN 55118', 'H3ID',
     'Dear Peter, my 2023 U.S. Congress Directory arrived in good order.', 'To help you fight corruption;', 'am',
     'enclosing a tax-deductible gift of:', 'Ds5o', '0S75', 'OS1OO', 'DS150', 'Ds20o DS250', 'DS', 'other',
     'Please make your check payable to:', 'National Legal and Policy Center"', 'or "NLPC"',
     'want t0 make a single gift today using my credit card. Please make', 'a one-time charge to my credit card of $',
     'Visa Q Mastorcard C Discover 0 AMEX', 'Card number', 'Expiralion date', 'Cardholder Signature',
     'want to enroll in the Monthly Gift Program. Please make a charge', 'io @iy Credit card of $', 'each; month',
     'understand thct', 'Mz;', 'Pso Mostan', '6061', 'BRADNER SMITH', '412/2623', '181J HLNE', 'Aftmnia', 'Fuct',
     '5348', 'Eh#_Natpna ( Leqal& Pluy Cexter_I $ 75,60', 'Seventy-fiveand', 'Dular5', 'NATIONAL BAnk',
     'Huld OUDNAIONALDO', 'nlpc.org', '#08E3000', 'J00z0805?4 p6o6', 'OLD'],
    ['Reply to Peter Flaherty', 'Chalrman; National Legal and Policy Center', 'From:', 'Ms. Theresa M: Couture',
     '903 Parma Way', 'Los Altos, CA 94024', 'H3IA', '4Dear Peter, my 2023 U.S',
     'Congress Directory arrived in good order.', 'To help', 'fight corruption;,', 'am enclosing', 'tax-C',
     '~deductible gift of:', '@s5o0 DS1,000', 'Ds2,500', 'Ds5,o0o DS10,000', 'DS', 'other',
     'Please make your check payable to:', '\'National Legal and Policy Center" or "NLPC"', 'THERESA M COUTLRE',
     '01-17', '2962', '141l4,77l0', 'GPAES', 'LCSALTOS, CA917', 'Aprill3122', 'Pa (u', 'Nhnxl_leydl', 'Polat Gutxr',
     '500', 'Orrr Q', 'fvehdrul', 'duly', 'Finst RE?UBLIC BANK', '41210816690', '800004E0?59w"', '0256', 'you'],
    ['Reply to Peter Flaherty', 'Chairman, National Legal and Policy Center', 'From:', 'Mrs. Elizabeth Eason',
     "123 Noah's Mill Road", 'Madison; MS 39110', 'H3IB',
     'Dear Peter, my 2023 U.S. Congress Directory arrived in good order.', 'To help you tight corruption,', 'am',
     'enclosing a tax-deductible gift of:', 'FS1OO', 'DS150', 'Ds200 Ds250', 'Ds5oo', 'DS1,000', 'Ds', 'other',
     'Please make your check', 'payable to:', '"National Legal and Policy Center" or "NLPC"',
     'want to make a single gift today using my credit card: Please make', 'one-time charge to my credit card of $_',
     'CVisa C #agiorcard 0 Dlscover D AMEX', 'Card number', 'Expiration date', 'Cardholder Signature',
     'want t0 enroll in the Monthly Gift Program: Please make', 'charge', 'to my credit card of $', 'each month:',
     'understand that', 'may', 'cancel at any time:', 'D Visa', 'Mastercard D Discover D AMEX', 'GENE', 'GENE BOTE;',
     'ELSON 06/00', 'EASON', '123 Noah a', '5771', 'MS 39110', '0314J', '4e/22', 'RERRE', 'eadl', 'Cubz', 'ALkred',
     '28', '00-', 'DOLLERS', 'vWW.nlpc org', 'REGIONS', '%OE53056380: 00086614', '105?61', 'LLdlt', 'Nakoczl', 'Bly'],
    ['Reply to Peter Flaherty', 'Chairman, National Legal and Policy Center', 'From:', 'Carole  Terry',
     '48513 Via Encanto', 'La Quinta, CA 92253-2259', 'HJIC',
     'QDear Peter, my 2023 U.S. Congress Directory arrived in good order:', 'To help you fight corruption,',
     'am enclosing a tax-deductible gift of:', 'DS1OO DS150', 'Dsz00', 'Ds250', 'Dsso0', 'Ds1.000', 'BS', '50', 'other',
     'Please make', 'check', 'payable to:', '"National Legal and Policy Center" or "NLPC"',
     'want to make a single gift today using my credit card. Please make', 'a one-time charge t0 my credit card of',
     'Visa', '0 Mastercard D Ciscover', 'AMEX', 'Card number', 'Expiration date', 'Cardholder Signature',
     'want to enroll in the Monthly Gift Program; Please make a charge', 'to my credit card of $_', 'each month:',
     'understand that', 'may', 'cancel at any time', 'Visa D Mastercard', 'DDiccouer', 'MEV', '8115', 'LLtal41',
     'CAROLE', '40767-4J0', '50', 'MAYo +2)', 'NLfC', 'Tallar', 'ELLY', '2e', 'nlpc org', '42!', '2707424 0832662907',
     'OB 445', 'your', 'WerRY', 'J $'],
    ['Reply to Peter Flaherty', 'Chairman', 'National Legal', 'and Policy Center', 'From:', 'Ms: Gail Bryan',
     '2639 Tahoe Dr', 'Livermore , CA 94550', 'P23286', 'Peter, my 2023 U.S. Congress Directory arrived in good',
     'order: To help you fight Biden and his allies,', 'am enclosing a', 'tax-deductible gift of:', 'Dssoo', 'DS1,000',
     'Ds2,500', 'Ds5,000', 'OS1O,000', 'S_300', 'ther', 'Please bill my credit card', 'Visa', '0 Mastercard',
     'D Discover 0 AMEX', 'Card number', 'Expiration date_', 'Cardholder Signature',
     'Please make your check payable to:', '"National Legal and Policy Center" or "NLPC"',
     'Please fold and return this reply along with your check', 'in the envelope provided:', '2-153*', 'account',
     'GAIl', 'BRYAN', '272', 'Z9 HdID4', 'LNJERVORE', 'Qaeen_Rat', 'DecLly303', '367', 'NatwonaL LegaldRysy Ceule',
     '5 30', '7/0', 'LnDLL', 'ncian', 'unlpc Org', '(tork # NuaekMaen', 'Fudorior Sbx To Withrk', '1 *A Ertat',
     'Yun "Iczea', 'uleter', 'LaaR', '403', '100', '574;', "70497221540'", '0272', 'Dear'],
    ['Reply to Peter Flaherty', 'Chalrman, National Legal and Policy Center', 'From:', 'Dr. Ronald D', 'Rowe',
     '55 Pasatiempo Dr.', 'Santa Cruz, CA 95060', 'HJIB', '@Dear Peter; my 2023 U.S. Congress Directory arrived in',
     'order.', 'To help you tight corruption;', 'am', 'enclosing a tax-deductible gift of:', 'D5100', 'Ds15O   Ds200',
     'Ds250', 'Dssoo', 'DS1,000', 'Ds', 'other', 'Please make your check payable to:',
     '"National Legal and Policy Center" or "NLPC"', 'want to make a single gift today using my credit', 'Please make',
     'one-time', 'charge to my credit card of $', 'C Visa', 'Mastercard', 'Q Discover 0 AMEX', 'Card number',
     'Expiration date_', 'Cardholder Signature', 'want to enroll in the Monthly Gift Program; Please make a charge',
     'to my credit card of $_', 'each month:', 'understand that', 'may', 'cancel at any time', 'Visa',
     'Mastercard 0 Discover 0 AMEX', 'RONALD D. ROWE', 'D.D.S:', '9624', 'PABATIEMFO DHIVE', 'S4TTA GUZ', 'Osne.',
     'DATE', '#Ik3', '02054', 'Baek', 'Hatunce Agsae', 'GenLz', 'Je', 'hendac_', '22', 'OLLIR $', 'Qurn Eua', 'FoA',
     'Loxka', 'K42Z', '"OO9Ezli\'', '0213?5221', 'BE5300', "S0E7'", 'good', 'card:', '0zlu', '36y', '76d'],
    ['Reply to Peter Flaherty', 'Chairman; National Legal and Pollicy Center', 'From:', 'Mr. Harvey Olney',
     '5213 County Road 1260', 'Lubbock; TX 79407', 'H3ID',
     'Dear Peter; my 2023 U.S. Congress Directory arrived in good order:', 'To help you fight corruption;', 'am',
     'enclosing a tax-deductible gift of:', 'Csso DS75', 'DS1O', 'DS150', 'Ds2oo 05250', 'DS_', 'other',
     'Please make your check payable to:', 'National Legal and Policy Center"', 'NLPC"',
     'want to make a single gift today using my credit card: Please make', 'a one-time charge to my credit card of $',
     'Visa QMastercard', 'Discover', 'AMEX', 'Card number', 'Expiration date', 'Cardholder Signature',
     'want t0 enroll in the Monthly Gift Program; Please make', 'charge', 'iU My', 'Ciedif Caid of $', 'cach month',
     'understand that', 'may:', 'cancel at any time.', 'HaaveY', 'OLNEY I', 'Zamt', '7040-280', '1594',
     'LULBOCX T7-I0r-F4e', '#tLze !', '"87135', 'Bruee', 'NLPc', '$ 50.0', 'FL', 'A/', 'MLL =', 'duln',
     'BANK OfAMErica', 'ChnC', '#nlpc org', 'Dmslez', '142/.7ODL++E.', '4odo0254', '00353208'],
    ['Reply to Peter Flaherty', 'Chairman; National Legal and Policy Center', 'G', 'From:', 'Dr. Cecil L Lemon',
     '514 Monterey Avenue', 'Odenton, MD 21113-1617', 'HJID', 'Dear Peter, my 2023 U.S:',
     'Congress Directory arrived in good order.', 'To help you fight corruption;',
     'am enclosing a tax-deductible gift of:', 'Ds5o   DS75', 'DS1OO', 'DS150', 'Ds200 0S250', 'DS_', '4d', 'other',
     'Please make your check payable to:', "National Legal and Policy Center'", 'Or "NLPC"',
     'want to make a single gift today using my credit card', 'Please make', 'one-time charge to my credit card of $',
     'Visa', 'Mastercard', '0 Discover', 'D AMEX', 'Card number_41LMLSN5S', 'Expiration date', 'Cardholder Signature',
     'want t0 enroll in the Monthly Gift Program: Please make a charge', 'to my credit card of $', 'each month_',
     'understand that | may', 'cancel at', 'time_', 'Visa', 'Mastercard', 'Discover', '0 AMEX', 'Card number',
     'Expiralion date_', 'Cardholder Signature', 'NLPC Taxpayer ID #52-1750188', 'NLPC', '107 Park Washington Court =',
     'Falls Church', '22046', '703-237-1970', 'tax 703-237-2090', 'e-mail: pflaherty @nlpc org', 'W" nipc org', 'UQ,',
     'Men', 'any'],
    ['Elebetty-', 'T6', 'LlWl', 'ULhellet1enel', 'Lu', 'YancLL', 'Zanr= DA,', 'EretudeML4a', 'Iuinstk', 'kLfLe', '2411',
     'Lott -', 'LuAkhLIrt', 'Daak', 'Fepel', '4(']
]

# def extractAddress(paragraph: List[str]):
#     replace_from = [' .', '.,', ' .,', ' ,', ',,', ';', ' ;', ':', ' :', '_', ' _']
#     replace_to = '.'
#     addr = None
#     for i, p in reversed(list(enumerate(paragraph))):
#         match = re.search(street_pattern, p)
#         post_match = re.search(po_box_pattern, p)
#         if match or post_match:
#             addr = match.group(0) if match else post_match.group(0)
#             addr = addr.rstrip()
#             for r in replace_from:
#                 addr = addr.replace(r, replace_to)
#             for s in street:
#                 addr = addr + '.' if addr.endswith(s) else addr
#
#     return addr
#
#
# def extractCityStateZipcode(name: str):
#     state = None
#     match = re.search(city_state_zip_pattern, name)
#     if match:
#         city = match.group('city')
#         state = match.group('state')
#         zip_code = match.group('zip')
#         state = {'city': city, 'state': state, 'zip': zip_code}
#
#     return state
#
#
# def extractTotalAddress(paragraph: List[str]):
#     total_address = {}
#     from_index = -1
#     to_index = -1
#
#     to_target = 'Dear Peter'
#     to_target_back = 'eter'
#
#     for i, p in enumerate(paragraph):
#         address_match = re.search(address_pattern, ''.join(p))
#         po_box_match = re.search(po_box_pattern, p)
#         if from_index == -1 and (po_box_match or address_match):
#             from_index = i
#
#         if to_index == -1 and (to_target in p or (i > 4 and to_target_back in p)):
#             to_index = i
#
#         if to_index != -1:
#             break
#
#     mail_code = None
#     code = None
#     address = None
#     if to_index != -1:
#         mail_code_index = to_index - 1
#         mail_code = paragraph[mail_code_index]
#
#         zip_code_index = mail_code_index - 1
#         city_state_zipcode = paragraph[zip_code_index]
#         check_before = paragraph[zip_code_index - 1]
#         if re.search(digit_start_pattern, city_state_zipcode) or re.search(state_start_patter, city_state_zipcode):
#             city_state_zipcode = check_before + ", " + city_state_zipcode
#             zip_code_index = zip_code_index - 1
#
#         replace_from = ['.', ' .', '.,', ' .,', ' ,', ',,', ';', ' ;', ':', ' :', '_', ' _']
#         replace_to = ','
#         for f in replace_from:
#             city_state_zipcode = city_state_zipcode.replace(f, replace_to)
#         for s in states:
#             city_state_zipcode = city_state_zipcode.replace(s + ",", s)
#             city_state_zipcode = city_state_zipcode.replace(s + " ,", s)
#             city_state_zipcode = city_state_zipcode.replace(s + ".", s)
#             city_state_zipcode = city_state_zipcode.replace(s + " .", s)
#
#         code = extractCityStateZipcode(city_state_zipcode)
#         address = extractAddress(paragraph[:zip_code_index])
#
#     if code is not None:
#         total_address.update(code)
#     if mail_code is not None:
#         total_address['mail_code'] = mail_code
#     if address is not None:
#         total_address['address'] = address
#     return total_address


class TestMyClass(unittest.TestCase):
    def test_something(self):
        # seperated
        for d in data:
            if isCommonForm(d):
                # extractNames(d)
                extractTotalAddress(d)
            elif isMailForm(d):
                pass


if __name__ == "__main__":
    unittest.main()
