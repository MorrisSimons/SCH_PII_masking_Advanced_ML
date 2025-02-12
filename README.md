preprocess 1 make NAME_1,NAME_N etc => NAME
preprocess 2 mashing

Location -> STREETADDRESS, SECONDARYADDRESS, BUILDINGNUMBER, STREET, CITY,STATE, COUNTY, NEARBYGPSCOORDINATE, ZIPCODE

GENDER = SEXTYPE, SEX

NAME = FULLNAME, FIRSTNAME, LASTNAME, CREDITCARDISSUER

IP = IPV4, IP, IPV6, MAC

JOB = JOBDESCRIPTOR, JOBTYPE, JOBTITLE, JOBAREA

MASKED_NUMBER = NUMBER, MASKED_NUMBER, AMOUNT, ACCOUNTNUMBER, CREDITCARDCVV, PIN, BUILDINGNUMBER

TODO: 

REMOVE: ORDINALDIRECTION, ACCOUNTNAME, CURRENCYSYMBOL, CURRENCYNAME, CURRENCY, CURRENCYCODE, CREDITCARDISSUER, ETHEREUMADDRESS, LITECOINADDRESS, BITCOINADDRESS

#### preprossesing
2. Scale down entities, ~~get mask enteties from tokens instead~~
3. Dataprepping, normalization, stemming or lemming -> Tokenization
4. Research Sentence splitting


#### EVAL
5. Eval model
6. Apply regex (test and eval it)

#### Extra
7. ~~ata vizualisation: Language Detection (språk)~~

1. AMAZON comprehend (morris intresserad)