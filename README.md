# ⚡ Mistral OCR

**Mistral OCR** is a plugin that permit to integrate the OCR model of Mistral AI into Grinning Cat.

### Plugin Configuration

The plugin offers several configurable parameters:

- **Mistral API KEY**: API key of Mistral
- **Save text to rabbit hole**: If enabled all image/pdf converted to Markdown by OCR are automatically ingested on rabbit hole

### Tech Info 

The plugin add some custom endpoints:

- **/custom/ocr**: Convert image to markdown
- **/custom/ocr-pdf**: Convert pdf to markdown
