<?php

if($_SERVER['REQUEST_URI'] == "/") {
	header("Location: /articles");
	die();
}

$uri = './data'.$_SERVER['REQUEST_URI'];

$content = null;
if(file_exists($uri.'.json'))
	$content = file_get_contents($uri.'.json');
else if(file_exists($uri.'/index.json'))
	$content = file_get_contents($uri.'/index.json');

if($content){
	header("Access-Control-Allow-Origin: *");
	header("content-type: application/json");
	echo $content;
} else {
	header("HTTP/1.0 404 Not Found");
	die('Page not found.');
}
