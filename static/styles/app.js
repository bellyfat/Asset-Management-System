var assets = parseInt(prompt("Please enter number of assets"));
// document.getElementById("id1").value=assets;
var element = document.getElementById("form1");
var i=0;
for(i=0;i<assets;i++)
{
element.innerHTML += "<input type='text' name='asset"+i+"' placeholder='add asset no "+(i+1)+"'><br>";
}
element.innerHTML += "<br><input type='submit' value='add'>";
s=""+assets;
document.getElementById("id1").value=s;
