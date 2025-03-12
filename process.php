<?php
if (isset($_GET['numbers']) && isset($_GET['threshold'])) {
    $numbers = escapeshellarg($_GET['numbers']);
    $threshold = escapeshellarg($_GET['threshold']);

    // Execute Python script
    $command = "python3 bitwise_operations.py $numbers $threshold";
    $output = shell_exec($command);

    // Decode JSON output
    $result = json_decode($output, true);

    if (isset($result['error'])) {
        echo "<h3>Error: {$result['error']}</h3>";
    } else {
        echo "<h1>Assignment7 - Results</h1>";
        echo "<h2>Integers separated by commas:</h2>";
        echo "<p>{$_GET['numbers']}</p>";
        echo "<h2>Threshold:</h2>";
        echo "<p>{$_GET['threshold']}</p><br>";
        echo "<h2>Bitwise Operation Results:</h2>";
        echo "<p>AND Operation Result: {$result['AND']}</p>";
        echo "<p>OR Operation Result: {$result['OR']}</p>";
        echo "<p>XOR Operation Result: {$result['XOR']}</p>";

        echo "<h2>Numbers Greater than Threshold:</h2>";
        if (!empty($result['Filtered'])) {
            echo "<p>[" . implode(", ", $result['Filtered']) . "]</p>";
        } else {
            echo "<p>No numbers above the threshold</p>";
        }
    }
} else {
    echo "<h3>Error: Missing input.</h3>";
}
?>