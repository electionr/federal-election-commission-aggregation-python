from flask import Flask
app = Flask(__name__)
app.debug = True
from flask import Response
@app.route("/")

#    <script type="text/javascript" src="/test.js"

def hello():
    return """
<html lang="en-US">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title>Test FEC</title>

  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>

    <script type="text/javascript">

    function mycallback(obj) {
    x = "<table>";
          x += "<tr><th>FIELD</th><th>VALUE</th></tr>";
        $("#mydata").html("<p>loading!");

          for (var field in obj) {
          v = obj[field];
          x += "<tr><td>" + field + "</td><td>" + v + "</td></tr>";
          }

          x += "</table>";
        $("#mydata").html("<p>loaded<p>" + x);

    };
(function($) {
var url = 'http://democr.us/fec/fech_py/lib/jsonp/_CONTRIBUTOR/CONTRIBUTOR_STATE/IL/CONTRIBUTOR_ZIP/60606/CONTRIBUTOR_CITY/Chicago/CONTRIBUTOR_STREET_1/20_S__Wacker_Drive/CONTRIBUTOR_ORGANIZATION_\
NAME/CME_Group_Inc__PAC/2011/20110504/727369.fec_1/AC5B039C2B6604D6B941.js';
$.ajax({
   type: 'GET',
    url: url,
    async: true,
    contentType: "application/json",
    dataType: 'jsonp',
    error: function(e) {
       console.log(e.message);
    }
});
})(jQuery);
    </script>
</head>
<body>
    <h1>Hello World!</h1>
    <p id="mydata"/>
    This is an example of loading a newly formatted json object
</body>

"""


@app.route("/test.js")
def test():
    return Response(
        """
        alert("load");
        mycallback( {"CONTRIBUTOR OCCUPATION": "", "CONTRIBUTION AMOUNT (F3L Bundled)": "136.67", "ELECTION CODE": "", "MEMO CODE": "", "CONTRIBUTOR EMPLOYER": "", "DONOR CANDIDATE STATE": "", "CONTRIBUTOR STREET 1": "215 Pennsylvania Avenue SE", "CONTRIBUTOR MIDDLE NAME": "", "DONOR CANDIDATE FEC ID": "", "DONOR CANDIDATE MIDDLE NAME": "", "CONTRIBUTOR STATE": "DC", "DONOR CANDIDATE FIRST NAME": "", "CONTRIBUTOR FIRST NAME": "", "BACK REFERENCE SCHED NAME": "", "DONOR CANDIDATE DISTRICT": "", "CONTRIBUTION DATE": "20110429", "DONOR COMMITTEE NAME": "", "MEMO TEXT/DESCRIPTION": "", "Reference to SI or SL system code that identifies the Account": "", "FILER COMMITTEE ID NUMBER": "C00113001", "DONOR CANDIDATE LAST NAME": "", "CONTRIBUTOR LAST NAME": "", "_record_type": "fec.version.v7_0.SA", "CONDUIT STREET2": "", "CONDUIT STREET1": "", "DONOR COMMITTEE FEC ID": "", "CONTRIBUTION PURPOSE DESCRIP": "Bank account interest", "CONTRIBUTOR ZIP": "20003", "CONTRIBUTOR STREET 2": "", "CONDUIT CITY": "", "ENTITY TYPE": "ORG", "CONTRIBUTOR CITY": "Washington", "CONTRIBUTOR SUFFIX": "", "TRANSACTION ID": "SA11AI.9560", "DONOR CANDIDATE SUFFIX": "", "DONOR CANDIDATE OFFICE": "", "CONTRIBUTION PURPOSE CODE": "", "ELECTION OTHER DESCRIPTION": "", "_src_file": "2011/20110504/727374.fec_1.yml", "CONDUIT STATE": "", "CONTRIBUTOR ORGANIZATION NAME": "Wachovia Bank", "BACK REFERENCE TRAN ID NUMBER": "", "DONOR CANDIDATE PREFIX": "", "CONTRIBUTOR PREFIX": "", "CONDUIT ZIP": "", "CONDUIT NAME": "", "CONTRIBUTION AGGREGATE F3L Semi-annual Bundled": "422.40", "FORM TYPE": "SA11AI"});
mycallback( {"CONTRIBUTOR OCCUPATION": "", "CONTRIBUTION AMOUNT (F3L Bundled)": "136.67", "ELECTION CODE": "", "MEMO CODE": "", "CONTRIBUTOR EMPLOYER": "", "DONOR CANDIDATE STATE": "", "CONTRIBUTOR STREET 1": "215 Pennsylvania Avenue SE", "CONTRIBUTOR MIDDLE NAME": "", "DONOR CANDIDATE FEC ID": "", "DONOR CANDIDATE MIDDLE NAME": "", "CONTRIBUTOR STATE": "DC", "DONOR CANDIDATE FIRST NAME": "", "CONTRIBUTOR FIRST NAME": "", "BACK REFERENCE SCHED NAME": "", "DONOR CANDIDATE DISTRICT": "", "CONTRIBUTION DATE": "20110429", "DONOR COMMITTEE NAME": "", "MEMO TEXT/DESCRIPTION": "", "Reference to SI or SL system code that identifies the Account": "", "FILER COMMITTEE ID NUMBER": "C00113001", "DONOR CANDIDATE LAST NAME": "", "CONTRIBUTOR LAST NAME": "", "_record_type": "fec.version.v7_0.SA", "CONDUIT STREET2": "", "CONDUIT STREET1": "", "DONOR COMMITTEE FEC ID": "", "CONTRIBUTION PURPOSE DESCRIP": "Bank account interest", "CONTRIBUTOR ZIP": "20003", "CONTRIBUTOR STREET 2": "", "CONDUIT CITY": "", "ENTITY TYPE": "ORG", "CONTRIBUTOR CITY": "Washington", "CONTRIBUTOR SUFFIX": "", "TRANSACTION ID": "SA11AI.9560", "DONOR CANDIDATE SUFFIX": "", "DONOR CANDIDATE OFFICE": "", "CONTRIBUTION PURPOSE CODE": "", "ELECTION OTHER DESCRIPTION": "", "_src_file": "2011/20110504/727374.fec_1.yml", "CONDUIT STATE": "", "CONTRIBUTOR ORGANIZATION NAME": "Wachovia Bank", "BACK REFERENCE TRAN ID NUMBER": "", "DONOR CANDIDATE PREFIX": "", "CONTRIBUTOR PREFIX": "", "CONDUIT ZIP": "", "CONDUIT NAME": "", "CONTRIBUTION AGGREGATE F3L Semi-annual Bundled": "422.40", "FORM TYPE": "SA11AI"});"""
        , mimetype='text/javascript'
)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8999)
