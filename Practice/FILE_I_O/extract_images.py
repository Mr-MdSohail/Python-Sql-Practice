import fitz # PyMuPDF
import os

def extract_images_from_pdf(pdf_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    # Open the PDF document
    doc = fitz.open(pdf_path)
    image_count = 0
    
    print(f"Opening '{pdf_path}' and searching for images...")
    
    # Iterate through every page in the PDF
    for page_index in range(len(doc)):
        page = doc[page_index]
        image_list = page.get_images(full=True)
        
        # Extract each image found on the page
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            # Save the image to the output folder
            image_filename = os.path.join(output_folder, f"image_p{page_index + 1}_{img_index + 1}.{image_ext}")
            with open(image_filename, "wb") as f:
                f.write(image_bytes)
                
            image_count += 1
            print(f"Saved: {image_filename}")
            
    print(f"\nExtraction complete! Successfully extracted {image_count} images into '{output_folder}'.")

if __name__ == "__main__":
    # Replace 'your_lab_manual.pdf' with the actual filename of your PDF
    pdf_file = r"C:\Users\moham\OneDrive\Desktop\Python\Practice\FILE_I_O\flutter_lab.pdf"
    output_dir = "extracted_images"
    
    extract_images_from_pdf(pdf_file, output_dir)