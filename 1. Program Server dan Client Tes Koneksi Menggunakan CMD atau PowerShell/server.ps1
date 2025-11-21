$listener = [System.Net.Sockets.TcpListener]::new(5050)
$listener.Start()
Write-Host "Server berjalan di port 5050..."
$client = $listener.AcceptTcpClient()

$stream = $client.GetStream()
$reader = [System.IO.StreamReader]::new($stream)
$writer = [System.IO.StreamWriter]::new($stream)
$writer.AutoFlush = $true

Write-Host "Client terhubung!"

while ($true) {
    $pesan = $reader.ReadLine()
    if ($pesan -ne $null) {
        Write-Host "Dari Client: $pesan"
        $writer.WriteLine("Server menerima: $pesan")
    }
}
