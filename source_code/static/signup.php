<?php 

require 'config.php';


try{
	$conn = new PDO('mysql:host=localhost;dbname=T', $config['DB_USERNAME'], $config['DB_PASSWORD']   );
	$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully"."<br>"; 
   
    $uname = $_POST['uname'];
	$pass = $_POST['pass'];
	$fname = $_POST['fname'];
	$lname = $_POST['lname'];
	$email = $_POST['email'];
	$dob = $_POST['dob'];
	$phno= $_POST['phno'];

	$gender = $_POST['gender'];
	
	
	echo "<br>Hello ".$uname." . <br />";
	
	$sql="INSERT INTO tornado VALUES ('$uname','$pass','$fname','$lname','$dob','$gender','$phno','$email')";
	$conn->exec($sql);
		echo "<br>Awesome...You are Registered sucessfully !";
		?>
		<html>
			<body>
			<a href="login.html"><br><br>
			<button name="login" id="login">Login</button>
			</a>
			</body>
		</html>
		<?php		

	} catch(PDOException $e){
		echo $sql."<br>". $e->getMessage();
		?>
		<html>
			<body>
			<a href="signup.html"><br><br>
			<button name="signup" id="signup">Try Again</button>
			</a>
			</body>
		</html>
		<?php		
	}

	
	$conn = null;

?>