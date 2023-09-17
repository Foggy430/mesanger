import asyncio
import websockets

connected = set()

async def echo(websocket, path):
    print("New connection established")
    connected.add(websocket)
    try:
        async for message in websocket:
            print(f"Received message: {message}")  # для отладки
            for conn in connected:
                if conn == websocket:
                    print(f"Sending message: {message}")  # для отладки
                    await conn.send(message)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connected.remove(websocket)

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())