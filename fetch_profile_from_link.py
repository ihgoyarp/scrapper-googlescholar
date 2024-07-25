import pandas as pd
from scholarly import scholarly

def fetch_profile_from_link(profile_link):
    # Mengambil profil penulis dari link
    author = scholarly.search_author_id(profile_link.split('user=')[1].split('&')[0])
    author = scholarly.fill(author)
    
    if author:
        print(f"Author: {author['name']}")
        print(f"Affiliation: {author['affiliation']}")
        print(f"Total Citations: {author['citedby']}")
        print(f"Publications:")
        print("-" * 80)
        
        # Mengumpulkan data publikasi
        publications_data = []
        for idx, pub in enumerate(author['publications'][:100], start=1):  # Batasi hasil ke 10 publikasi pertama
            pub = scholarly.fill(pub)
            title = pub['bib']['title']
            url = pub.get('pub_url', 'No URL available')
            accreditation = "N/A"  # Replace with actual accreditation if available
            year = pub['bib'].get('pub_year', 'No year available')
            pub_type = pub['bib'].get('type', 'No type available')
            
            publications_data.append([idx, title, url, accreditation, year, pub_type])
            
            # Print to console (optional)
            print(f"No: {idx}")
            print(f"Title: {title}")
            print(f"URL: {url}")
            print(f"Accreditation: {accreditation}")
            print(f"Year: {year}")
            print(f"Type: {pub_type}")
            print("-" * 80)
        
        # Membuat DataFrame dari data publikasi
        df = pd.DataFrame(publications_data, columns=["No", "Judul", "URL / Alamat", "Akreditasi", "Tahun", "Jenis"])
        
        # Menyimpan DataFrame ke file Excel
        file_name = f"{author['name']}_publications.xlsx"
        df.to_excel(file_name, index=False)
        
        print(f"Data saved to {file_name}")
    else:
        print("Author not found.")

if __name__ == "__main__":
    profile_link = input("Masukkan link profil Google Scholar: ")
    fetch_profile_from_link(profile_link)
