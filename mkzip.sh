
#!/bin/bash

# Source vars.conf to get all the stored variables
source vars.conf

# Change Current Directory to AnyKernel3
cd "/home/folder/android/AnyKernel"

git reset --hard
git clean -f -d
KERNEL_DIR=/home/folder/android/kernels/msm-4.9
# Change anykernel script values
sed -i "s|^kernel.string=.*|kernel.string=$kstring|g" "/home/folder/android/AnyKernel/anykernel.sh"
sed -i "s|^device.name1=.*|device.name1=$dname|g" "/home/folder/android/AnyKernel/anykernel.sh"
sed -i "s|^block.*|block=$block;|g" "/home/folder/android/AnyKernel/anykernel.sh"
sed -i "s|^supported.versions=.*|supported.versions=|g" "/home/folder/android/AnyKernel/anykernel.sh"
sed -i "s|^supported.patchlevels=.*|supported.patchlevels=|g" "/home/folder/android/AnyKernel/anykernel.sh"
sed -i '/# begin ramdisk changes/,/# end ramdisk changes/d' "/home/folder/android/AnyKernel/anykernel.sh"
sed -i 's/toro//g' "/home/folder/android/AnyKernel/anykernel.sh"
sed -i 's/plus//g' "/home/folder/android/AnyKernel/anykernel.sh"
sed -i 's/tuna//g' "/home/folder/android/AnyKernel/anykernel.sh"

# Copy zIMAGE/Image.gz-dtb from kernel out
mv $KERNEL_DIR/out/arch/arm64/boot/Image.gz-dtb /home/folder/android/AnyKernel/Image.gz-dtb
mv $KERNEL_DIR/out/arch/arm/boot/zImage /home/folder/android/AnyKernel/zImage

# Create AnyKernel Zip
zip -r9 $ZIPNAME * -x .git README.md
echo -e "\e[1;32mFlashable ZIP Created Succesfully\e[0m"
