<?php 

require 'config.php';

	$conn = new mysqli('localhost','root','root','T');
	if($conn->connect_error){die("Connection Failed : ".$conn->connect_error);}
		echo "Successfully Connected to the Database."."<br />";
    
    
    $uname = $_POST['uname'];
	$pass = $_POST['pass'];

	echo "<br>Hello ".$uname.". Please Wait while we Authenticate You...<br />";

	$sql = "SELECT pass FROM tornado WHERE username = '".$uname."' and pass = '".$pass."'";
	$result = $conn->query($sql);
	if($result->num_rows > 0){
		echo "<br>You are Successfully Logged In ! Welcome...<br />";
	}

	else 
		{ echo  "<br>Invalid Username or Password. Try again...<br />";
		?>
		<html>
			<body>
			<a href="login.html"><br><br>
			<button name="login" id="login">Login</button>
			</a>
			</body>
		</html>
		<?php	 }


	
	$conn = null;



?>