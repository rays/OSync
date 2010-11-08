<?PHP
$json_file = file_get_contents("osync.json");
print_r($json_file);
$json = json_decode($json_file, true);
var_dump($json);
// echo $_GET['callback'] . '(' . $json_file . ');';