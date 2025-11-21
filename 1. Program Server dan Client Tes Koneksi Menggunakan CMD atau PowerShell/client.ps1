$client = [System.Net.Sockets.TcpClient]::new()
$client.Connect("127.0.0.1", 5050)

$stream = $client.GetStream()
$reader = [System.IO.StreamReader]::new($stream)
$writer = [System.IO.StreamWriter]::new($stream)
$writer.AutoFlush = $true

Write-Host "Terhubung ke server!"

while ($true) {
    $pesan = Read-Host "Ketik pesan untuk server"
    $writer.WriteLine($pesan)

    $balasan = $reader.ReadLine()
    if ($balasan -ne $null) {
        Write-Host "Balasan server: $balasan"
    }
}
