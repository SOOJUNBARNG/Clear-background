import aspose.words as aw

def convert_png_to_svg(input_path, output_path):
    # Create a document and a document builder
    doc = aw.Document()
    builder = aw.DocumentBuilder(doc)

    # Insert the image into the document
    shape = builder.insert_image(input_path)

    # Save the document as SVG
    doc.save(output_path)
    print(f"Conversion complete: {output_path}")

convert_png_to_svg('logo.png', 'output.svg')