<?php
//-----------------------------------------------------------------------------------
// PARAMETRI DI CONFIGURAZIONE GENERALE
//-----------------------------------------------------------------------------------
$emailAdmin = "your.address@your.domain.com";  // email admin where notices are sent
$urlWebSite = "www.example.com"; //Website URL that is added to the bottom of emails sent from contact form

$headers_mail = "From: Company Name <info@your_domain.com>\nReply-to:info@your_domain.com";
define("OGGETTO_MAIL", "Contact from the site.");

########################################################################
/*#################		TEMPLATE MAIL		##########################*/
########################################################################
$str_contenuto_email = "
You are receiving this email because someone used the card of contacts on your website.

Here the personal information that we have contacted:

-------------------------------------------------------------
Name and Surname: {name}
E-mail: {mail}
IP Address: {ip}
-------------------------------------------------------------

This is the user's request:

-------------------------------------------------------------
Message: {corpo}
-------------------------------------------------------------

{url}";
?>