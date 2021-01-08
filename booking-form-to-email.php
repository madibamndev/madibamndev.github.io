<?php
if(!isset($_POST['submit']))
{
	//This page should not be accessed directly. Need to submit the form.
	echo "error; you need to submit the form!";
}
$first_name = $_POST['first_name'];
$last_name = $_POST['last_name'];
$visitor_email = $_POST['email'];
$phone_number = $_POST['number'];
$type_of_service = $_POST['name'];
$additional_information = $_POST['message'];
$booking_date = $_POST['date'];
$booking_time = $_POST['time'];

//Validate first
if(empty($first_name)) 
{
    echo "First Name is mandatory!";
    exit;
}

if(empty($last_name))
{
    echo "Last Name is mandatory!";
    exit;
}

if(empty($visitor_email))
{
    echo "Valid email is mandatory!";
    exit;
}

if(IsInjected($visitor_email))
{
    echo "Bad email value!";
    exit;
}

if(empty($phone_number))
{
    echo "Valid phone number is mandatory!";
    exit;
}

if(empty($type_of_service))
{
    echo "Select a service!";
    exit;
}

if(empty($booking_date))
{
    echo "Select a suitable date!";
    exit;
}

if(empty($booking_time))
{
    echo "Select a suitable time!";
    exit;
}

$email_from = 'vjnisokalakasee254@gmail.com';//<== update the email address
$email_subject = "New Form submission";
$email_body = "You have received a new booking from $name.\n".
    "Here is the booking message:\n $first_name, $last_name, $visitor_email, $phone_number, $type_of_service, $additional_information, $booking_date, $booking_time".
    
$to = "vjnisokalakasee254@gmail.com";//<== update the email address
$headers = "From: $email_from \r\n";
$headers .= "Reply-To: $visitor_email \r\n";
//Send the email!
mail($to,$email_subject,$email_body,$headers);
//done. redirect to thank-you page.
header('Location: thankyou.html');


// Function to validate against any email injection attempts
function IsInjected($str)
{
  $injections = array('(\n+)',
              '(\r+)',
              '(\t+)',
              '(%0A+)',
              '(%0D+)',
              '(%08+)',
              '(%09+)'
              );
  $inject = join('|', $injections);
  $inject = "/$inject/i";
  if(preg_match($inject,$str))
    {
    return true;
  }
  else
    {
    return false;
  }
}  
?> 