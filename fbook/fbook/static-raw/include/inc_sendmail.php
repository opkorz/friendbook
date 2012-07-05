<?php
include_once("config.php");
//------------------------------------------------------------------------------------------------
// RECUPERO IL VALORE DI TUTTI I DATI INVIATI DALL'UTENTE
//------------------------------------------------------------------------------------------------
$str_ind_ip = $_SERVER['REMOTE_ADDR'];
foreach ($_POST as $key=>$value) {
	$$key = $value;
}
//------------------------------------------------------------------------------------------------
//  PROCEDURA DI INVIO MAIL
//-------------------------------------
$str_oggetto			= OGGETTO_MAIL;
$str_contenuto_email 	= str_replace("{name}",$visitor,$str_contenuto_email);
$str_contenuto_email 	= str_replace("{mail}",$visitormail,$str_contenuto_email);
$str_contenuto_email 	= str_replace("{ip}", $str_ind_ip,$str_contenuto_email);
$str_contenuto_email 	= str_replace("{corpo}",$notes,$str_contenuto_email);
$str_contenuto_email 	= str_replace("{url}",$urlWebSite,$str_contenuto_email);
$headers				= $headers_mail;

if (!@mail($emailAdmin,$str_oggetto,$str_contenuto_email,$headers)) {
	echo "<div class=\"error\">Have been some problems sending the email.</div>";
} else {
    echo "<div class=\"success\">The email has been sent successfully.</div>";
}