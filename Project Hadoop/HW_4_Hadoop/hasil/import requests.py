import requests
import asyncpg
import asyncio
import csv
import nest_asyncio

# Mengizinkan nested event loop
nest_asyncio.apply()

# Konfigurasi Database
DATABASE_URL = "postgresql://postgres:12345678@localhost/pokeability"

# Pool Koneksi Database Asinkron
async def get_pool():
    return await asyncpg.create_pool(DATABASE_URL)

# Mengambil dan Menyimpan Data Kemampuan Pokemon
async def fetch_and_store_ability(pool, pokemon_ability_id):
    try:
        url = f"https://pokeapi.co/api/v2/ability/{pokemon_ability_id}"
        call = requests.get(url)
        call.raise_for_status()  # Raise an HTTPError for bad responses
        response = call.json()

        records = []
        async with pool.acquire() as conn:
            for effect_entry in response['effect_entries']:
                await conn.execute("""
                    INSERT INTO pokemon_effect (pokemon_ability_id, effect, language, short_effect)
                    VALUES ($1, $2, $3, $4);
                """, int(pokemon_ability_id), str(effect_entry['effect']), 
                str(effect_entry['language']['name']), str(effect_entry['short_effect']))
                records.append({
                    "pokemon_ability_id": pokemon_ability_id,
                    "effect": effect_entry['effect'],
                    "language": effect_entry['language']['name'],
                    "short_effect": effect_entry['short_effect']
                })
        
        print(f"Saved ability_id {pokemon_ability_id} to database")
        return records
    except requests.exceptions.RequestException as e:
        print(f"HTTP error fetching ability_id {pokemon_ability_id}: {str(e)}")
        return []
    except Exception as e:
        print(f"Error saving ability_id {pokemon_ability_id}: {str(e)}")
        return []

# Fungsi untuk menyimpan hasil ke CSV
def save_to_csv(data, filename='pokemon_abilities.csv'):
    fieldnames = ['pokemon_ability_id', 'effect', 'language', 'short_effect']
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for record in data:
            writer.writerow(record)

# Fungsi Utama
async def main():
    pool = await get_pool()
    tasks = [fetch_and_store_ability(pool, pokemon_ability_id) for pokemon_ability_id in range(1, 1000)]
    results = await asyncio.gather(*tasks)
    all_records = [record for result in results for record in result]
    print("Completed fetching and storing abilities")
    
    # Simpan hasil ke CSV
    save_to_csv(all_records)

# Menjalankan Skrip
if __name__ == "__main__":
    asyncio.run(main())
