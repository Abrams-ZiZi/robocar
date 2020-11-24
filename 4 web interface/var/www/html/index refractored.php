<html>
<head>
<script Language="Javascript">
function set_left()
{
    document.location="cgi-bin/set_left.cgi";
}
function set_right()
{
    document.location="cgi-bin/set_right.cgi";
}
function set_forward()
{
    document.location="cgi-bin/set_forward.cgi";
}
function set_reverse()
{
    document.location="cgi-bin/set_reverse.cgi";
}
function stop(event)
{
    document.location="cgi-bin/stop.cgi";
}
</script>
</head>


<body>
<div style="text-align:center">
  <h1>Raspberry Pi GPIO</h1>
 
  <img src="/arrow_forward.jpg" id="f" onpointerdown="set_forward()" onpointerup="stop()">
  <br>
  <img src="/arrow_left.jpg" id="l" onpointerdown="set_left()" onpointerup="stop()">
  <img src="/arrow_right.jpg" id="r" onpointerdown="set_right()" onpointerup="stop()">
  <br>
  <img src="/arrow_reverse.jpg" id="r" onpointerdown="set_reverse()" onpointerup="stop()">
  <br>
  <img src="/stop.jpg" id="s" onpointerdown="stop()" onpointerup="stop()">
  </div>
  </body>
</html>


