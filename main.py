from mcstatus import JavaServer

host = '127.0.0.1'
port = '25565'
address = host + ':' + port
timeout = 3

try:
    server = JavaServer.lookup(address, timeout)

    print(f'ไอพีเซิร์ฟเวอร์ คือ {server.address.host}')
    print(f'หมายเลขพอร์ตเซิร์ฟเวอร์ คือ {server.address.port}')
    print(f'ระยะเวลารอเชื่อมต่อสูงสุด {server.timeout} วินาที ก่อนการเชื่อมต่อจะล้มเหลว')

    status = server.status()
    print(f'ผู้เล่นออนไลน์ทั้งหมด {status.players.online} / {status.players.max} คน')
    print(f'ชื่อเวอร์ชัน คือ {status.version.name}')
    print(f'โปรโตคอล คือ {status.version.protocol}')
    print(f'ความหน่วงระหว่างเซิร์ฟเวอร์ส่วนตัวกับผู้เล่น {status.latency} มิลลิวินาที')

    latency = server.ping()
    print(f'ความหน่วงระหว่างเซิร์ฟเวอร์ Minecraft Java Edition กับผู้เล่น {latency} มิลลิวินาที')

    query = server.query()
    print(f'ผู้เล่นออนไลน์ทั้งหมด {query.players.online} / {query.players.max} คน')
    if len(query.players.names) != 0:
        print(f'ผู้เล่นที่กำลังออนไลน์มีดังนี้')
        for player in query.players.names:
            print(player)
    else:
        print('ไม่มีผู้เล่นที่กำลังออนไลน์ในเซิร์ฟเวอร์')
    print(f'เวอร์ชันเซิร์ฟเวอร์ คือ {query.software.version}')
    print(f'ยี่ห้อเซิร์ฟเวอร์ที่ใช้งาน คือ {query.software.brand}')
    if len(query.software.plugins) != 0:
        print(f'ปลั๊กอินที่ใช้ทั้งหมดในเซิร์ฟเวอร์มีดังนี้')
        for plugin in query.software.plugins:
            print(plugin)
    else:
        print('ไม่มีปลั๊กอินที่ใช้ในเซิร์ฟเวอร์')
    for plugin in query.software.plugins:
        print(plugin)
    print(f'ชื่อแผนที่ {query.map}')

except Exception as e:
    print(e)