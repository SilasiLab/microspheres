	waitForUser("Choose working directory");
	dir = getDirectory("Choose source directory");


autocheck=false;
enhancecheck=false;
thresholdcheck=false;
consolidatecheck=false;
roicheck=false;
beadcheck=false;
visualcheck=false;
verifycheck=false;
ROIcountcheck=false;
dimensioncheck=false;
volumecheck=false;


Dialog.create("Identify Processing Step");
Dialog.addMessage("***EACH STEP MUST BE COMPLETED IN ORDER TO MOVE ON TO THE NEXT***");
Dialog.addMessage("QUINT WORKFLOW");
Dialog.addCheckbox("1.1) Automatically align images using 'StackReg' plugin and rename images for 'File Builder'", autocheck);
Dialog.addCheckbox("1.2) If necessary, enhance brightness of coloured images", enhancecheck);
Dialog.addMessage("       2) Run 'File Builder'");
Dialog.addMessage("       3) Anchor serial blockface images using 'Quick NII'");
Dialog.addCheckbox("4) Threshold images to detect microspheres", thresholdcheck);
Dialog.addCheckbox("5) Manually divide ROI by hemisphere", roicheck);
Dialog.addCheckbox("6) Determine true microsphere location and resize microsphere segmentation map for 'Nutil' (make sure QuickNII atlas images are saved)", consolidatecheck);
Dialog.addMessage("       7) Register microspheres with 'Nutil'");
Dialog.addCheckbox("8) Determine area of coronal images", volumecheck);
Dialog.addMessage("VALIDATION OPTIONS");
Dialog.addCheckbox("1) Manually label microspheres to validate bead thresholding", beadcheck);
Dialog.addCheckbox("2) Visually validate bead thresholding", visualcheck);
Dialog.addCheckbox("3) Compare manual counts to thresholded counts", verifycheck);
Dialog.addCheckbox("4) Produce ROI of each consolidated microsphere from manual counts", ROIcountcheck);
Dialog.addMessage("RESIZE A SEGMENTATION MAP FOR NUTIL:");
Dialog.addCheckbox("1) Select a segmentation map folder and resize to match dimensions of atlas images produced from 'Quick NII'", dimensioncheck);



Dialog.show();
autocheck = Dialog.getCheckbox();
enhancecheck = Dialog.getCheckbox();;
thresholdcheck = Dialog.getCheckbox();;;
roicheck = Dialog.getCheckbox();;;;
consolidatecheck = Dialog.getCheckbox();;;;;
volumecheck = Dialog.getCheckbox();;;;;;
beadcheck = Dialog.getCheckbox();;;;;;;
visualcheck = Dialog.getCheckbox();;;;;;;;
verifycheck = Dialog.getCheckbox();;;;;;;;;
ROIcountcheck = Dialog.getCheckbox();;;;;;;;;;
dimensioncheck = Dialog.getCheckbox();;;;;;;;;;;


if (File.exists(dir+"1-Raw Images")) {
} else {
	File.makeDirectory(dir+"1-Raw Images");
	}
rawdir = dir+"1-Raw Images"+File.separator;

if (File.exists(dir+"2.1-Aligned Images")) {
} else {
	File.makeDirectory(dir+"2-Aligned Images");
	}
autodir = dir+"2-Aligned Images"+File.separator;

sH = screenHeight;
sW = screenWidth;

if (autocheck == true) {

	cage = getNumber ("Enter the animal's cage number", 0); 
	id = getNumber ("Enter the animal's ID", 0);

	
	rawimages = getFileList(rawdir);
	Array.sort(rawimages);


	for (i = 0; i < rawimages.length; i++) {
		open(rawdir + rawimages[i]);
		}
	
	setBackgroundColor(0, 0, 0);	

	run("Images to Stack", "name=Stack title=[] use");
	imgName=getTitle();
	selectWindow(imgName);
	setLocation(0,0);

	// If rotating the image cuts off the brain, you can make the dimension of the image larger below:
	run("Canvas Size...", "width=3000 height=1944 position=Center");
	
	setTool("line");
	waitForUser("Draw a vertical line (top-down) through the midline of the brain & choose a centred posterior image (all images will be aligned to this image) and press OK");
	run("Measure");
	angle = getResult("Angle");
	corrangle = angle+90;
	selectWindow("Results");
	run("Close");
	run("Rotate... ", "angle=corrangle grid=1 interpolation=Bilinear stack");
	run("Select None");

	run("StackReg ", "transformation=[Rigid Body]");
	run("Image Sequence... ", "format=TIFF start=1 digits=3 save=autodir");

	close();

	images = getFileList(autodir);
	Array.sort(images);

	if (File.exists(autodir + cage + "-" + id + "_colour")) {
	} else {
		File.makeDirectory(autodir + cage + "-" + id + "_colour");
		}
	colourdir = autodir + cage + "-" + id + "_colour" + File.separator;

	if (File.exists(autodir + cage + "-" + id + "_green")) {
	} else {
		File.makeDirectory(autodir + cage + "-" + id + "_green");
		}
	greendir = autodir + cage + "-" + id + "_green" + File.separator;

	for (a=0; a<images.length; a++){
		open(autodir + images[a]);
		
		fileName=getTitle();
		num = substring(fileName, 5, 8);	
		saveAs("jpg", colourdir + cage + "-" + id + "_s" + num);

		run("Split Channels");
		selectWindow(fileName + " (blue)");
		close();
		selectWindow(fileName + " (red)");
		close();
		selectWindow(fileName + " (green)");
		saveAs("jpg", greendir + cage + "-" + id + "_s" + num);
		close();

		File.delete(autodir + images[a]);
	}

	selectWindow("Log");
	run("Close");

	if (File.exists(dir+"~Export Slices (from Quick NII)")) {
	} else {
		File.makeDirectory(dir+"~Export Slices (from Quick NII)");
		}
	slicedir = dir+"~Export Slices (from Quick NII)"+File.separator;
}

if (enhancecheck == true){

	//waitForUser("Choose directory containing images that you want brightened");
	//colourdir=getDirectory("Directory containing images to be brightened");
	
	autodirlist=getFileList(autodir);
	colourdir=autodir + autodirlist[0];
	colouredimages = getFileList(colourdir);
	
	Array.sort(colouredimages);



	for (i = 0; i < colouredimages.length; i++) {
		open(colourdir + colouredimages[i]);
	}

	//fileName=getTitle();
	//end=indexOf("s", fileName);
	//print(end);
	//print(fileName);
	//brainID = substring(fileName, 0, end);

	run("Images to Stack", "name=Stack title=[] use");

	run("Brightness/Contrast...");
	waitForUser("Adjust brightness to improve identification of internal stuctures and press OK");
	min = getNumber ("Enter min brightness:", 0);
	max = getNumber ("Enter max brightness:", 255);
	setMinAndMax(min, max);
	run("Apply LUT", "stack");


	if (File.exists(colourdir + "Brightened")) {
	} else {
		File.makeDirectory(colourdir + "Brightened");
		}
	enhancedir = colourdir + "Brightened" + File.separator;

	run("Image Sequence... ", "format=JPG save=enhancedir");
	close();

	renameimages=getFileList(enhancedir);
	Array.sort(renameimages);

	for (i = 0; i < renameimages.length; i++) {
		File.rename(enhancedir + renameimages[i], enhancedir + colouredimages[i]);
	}
	close("Log");
	
	
}

if (thresholdcheck == true) {

	cage = getNumber ("Enter the animal's cage number", 0); 
	id = getNumber ("Enter the animal's ID", 0);
	Dialog.create("Split Colour Channel?");
  	GreenOnly = newArray("Yes", "No");
  	Dialog.addRadioButtonGroup("Run bead threshold on green channel?", GreenOnly, 1, 2, "Yes");
  	Dialog.show;
	GreenOnly = Dialog.getRadioButton;
	
	
	if (File.exists(dir+"3-Thresholded Image")) {
	} else {
		File.makeDirectory(dir+"3-Thresholded Image");
		}
	thresholddir = dir+"3-Thresholded Image"+File.separator;

colourdir = autodir + cage + "-" + id + "_colour" + File.separator;
greendir = autodir + cage + "-" + id + "_green" + File.separator;

	if(GreenOnly=="No"){
	renamedImages=getFileList(colourdir);
	Array.sort(renamedImages);
	
		for (i = 0; i < renamedImages.length; i++) {
			open(colourdir + renamedImages[i]);
			fileName=getTitle();
			run("8-bit");
			//mouse
			setThreshold(0, 75);
			//rat
			//setThreshold(0, 75);
			run("Convert to Mask");
			run("Invert");
			run("Despeckle");
			saveAs("png", thresholddir + fileName);
			close();
		}

	} else {
		renamedImages=getFileList(greendir);
		Array.sort(renamedImages);
		
		for (i = 0; i < renamedImages.length; i++) {
			open(greendir + renamedImages[i]);
			fileName=getTitle();
			run("8-bit");
			//mouse //125
			//setThreshold(0, 75);
			//setThreshold(0, 140);
			//setThreshold(0, 150);
			setThreshold(0, 170);
			
			run("Convert to Mask");
			run("Invert");
			run("Despeckle");
			saveAs("png", thresholddir + fileName);
			close();
		}
		
	}




	if (File.exists(dir+"~Export Slices (from Quick NII)")) {
	} else {
		File.makeDirectory(dir+"~Export Slices (from Quick NII)");
		}
	slicedir = dir+"~Export Slices (from Quick NII)"+File.separator;
	
}

if (roicheck == true){
	alignedBFdir=dir+"2-Aligned Images"+File.separator;
	alignedBF1=getFileList(alignedBFdir);
	//alignedBFdir2=alignedBFdir+alignedBF1[0];
	alignedBFdir2=alignedBFdir+alignedBF1[1];
	alignedBF2=getFileList(alignedBFdir2);

	if (File.exists(alignedBFdir + "ROIs")) {
	} else {
		File.makeDirectory(alignedBFdir + "ROIs");
		}
	ROIdir = alignedBFdir + "ROIs" + File.separator;
	
	slicedir = dir+"~Export Slices (from Quick NII)"+File.separator;
	thresholddir = dir+"3-Thresholded Image"+File.separator;
	images = getFileList(thresholddir);
	Array.sort(images);

	//if (File.exists(thresholddir + "Consolidated Images")) {
	//} else {
	//	File.makeDirectory(thresholddir + "Consolidated Images");
	//	}
	//consolidateddir = thresholddir + "Consolidated Images" + File.separator;

	//if (File.exists(consolidateddir + "Left Hemisphere")) {
	//} else {
	//	File.makeDirectory(consolidateddir + "Left Hemisphere");
	//	}
	//LeftHemdir = consolidateddir + "Left Hemisphere" + File.separator;

	//if (File.exists(consolidateddir + "Right Hemisphere")) {
	//} else {
	//	File.makeDirectory(consolidateddir + "Right Hemisphere");
	//	}
	//RightHemdir = consolidateddir + "Right Hemisphere" + File.separator;

//Creates an ROI of each hemisphere to faciliate comparing hemispheric differences.

//based on number of existing xml files within folder
	//stop=alignedBF2.length-3;
		
	stop=alignedBF2.length;

		for (i = 0; i < stop; i++) {
			open(alignedBFdir2+alignedBF2[i]);
		
			imageName=getTitle();
			//end=indexOf(imageName, ".jpg");
			//imageName2=substring(imageName, 0, end);
		
			run("Duplicate...", " ");
			duplicateTitle=getTitle();
			
			//Threshold option
			//run("8-bit");
			//setAutoThreshold("Default");
			//run("Threshold...");
			//setThreshold(10, 255);
			//run("Convert to Mask");
		
			//Binary option
			run("Make Binary");
			run("Fill Holes");
			run("Dilate");
			run("Dilate");
			run("Dilate");
			run("Dilate");
			run("Dilate");
			run("Dilate");
			run("Dilate");
			run("Dilate");
			run("Dilate");
			run("Dilate");
			
			//close("Threshold");
		
			run("Analyze Particles...", "size=100000-Infinity summarize add");
			close("Summary");
			
			close(duplicateTitle);			
		
			//setTool("polygon");
			setTool("rectangle");
			waitForUser("Draw a square (or use the polygon tool) containing only the left hemisphere (actual right hemisphere), press ok");
			roiManager("Add");
			roiManager("Select", newArray(0,1));
			roiManager("AND");
			roiManager("Add");
			roiManager("Select", newArray(0,2));
			roiManager("XOR");
			roiManager("Add");
			roiManager("Select", 1);
			roiManager("Delete");
			roiManager("Select", 0);
			roiManager("rename", "Both Hemi");
			roiManager("Select", 2);
			roiManager("rename", "Left Hemi");
			roiManager("Select", 1);
			roiManager("rename", "Right Hemi");
			selectWindow("ROI Manager");
			roiManager("Save", ROIdir + imageName + ".zip");
			
			selectWindow("ROI Manager");
			run("Close");
			run("Close All");	
		}


		
}


if (consolidatecheck == true) {
////////////////////////////////////////////////////////////////////////////////////////////
	
	alignedBFdir=dir+"2-Aligned Images"+File.separator;
	alignedBF1=getFileList(alignedBFdir);
	//alignedBFdir2=alignedBFdir+alignedBF1[0];
	alignedBFdir2=alignedBFdir+alignedBF1[1];
	alignedBF2=getFileList(alignedBFdir2);

	if (File.exists(alignedBFdir + "ROIs")) {
	} else {
		File.makeDirectory(alignedBFdir + "ROIs");
		}
	ROIdir = alignedBFdir + "ROIs" + File.separator;
	
	slicedir = dir+"~Export Slices (from Quick NII)"+File.separator;
	thresholddir = dir+"3-Thresholded Image"+File.separator;
	images = getFileList(thresholddir);
	Array.sort(images);

	if (File.exists(thresholddir + "Consolidated Images")) {
	} else {
		File.makeDirectory(thresholddir + "Consolidated Images");
		}
	consolidateddir = thresholddir + "Consolidated Images" + File.separator;

	if (File.exists(consolidateddir + "Left Hemisphere")) {
	} else {
		File.makeDirectory(consolidateddir + "Left Hemisphere");
		}
	LeftHemdir = consolidateddir + "Left Hemisphere" + File.separator;

	if (File.exists(consolidateddir + "Right Hemisphere")) {
	} else {
		File.makeDirectory(consolidateddir + "Right Hemisphere");
		}
	RightHemdir = consolidateddir + "Right Hemisphere" + File.separator;

//always subtract at least 1 because the last image in series cannot be subtracted from anything
//based on number of existing xml files within folder subtract more from this number
	stop=images.length-1;

ROIlist=getFileList(ROIdir);

	for (i = 0; i < stop; i++) {
		open(thresholddir + images[i]);
		image1=getTitle();
		open(thresholddir + images[i+1]);
		image2=getTitle();
		selectWindow(image2);
		run("Dilate");
		run("Dilate");
		run("Dilate");
		run("Dilate");
		imageCalculator("Subtract create", image1,image2);
		close(image1);
		close(image2);
		run("Despeckle");
		run("Despeckle");
		run("Despeckle");


///////
	imageName=getTitle();
	run("Colors...", "foreground=black background=white selection=green");
	selectWindow(imageName);
	run("Duplicate...", " ");
	duplicateTitle=getTitle();

	open(ROIdir+ROIlist[i]);


	roiManager("Select", 2);
	run("Clear Outside");
	saveAs("png", LeftHemdir + image1);
	close(image1);

	selectWindow(imageName);
	run("Duplicate...", " ");
	duplicateTitle=getTitle();

	roiManager("Select", 1);
	run("Clear Outside");
	saveAs("png", RightHemdir + image1);
	close(image1);

	close(imageName);


	selectWindow("ROI Manager");
	run("Close");
	}

// since the last image has nothing to substract from.
	open(thresholddir + images[stop]);
	image=getTitle();

	run("Duplicate...", " ");
	duplicateTitle=getTitle();

	open(ROIdir+ROIlist[stop]);
	roiManager("Select", 2);
	run("Clear Outside");
	saveAs("png", LeftHemdir + image);
	close(duplicateTitle);

	roiManager("Select", 1);
	run("Clear Outside");
	saveAs("png", RightHemdir + image);
	close(duplicateTitle);
	close(image);

	selectWindow("ROI Manager");
	run("Close");
	
////////resize thresholded images

	RightHemList=getFileList(RightHemdir);
	LeftHemList=getFileList(LeftHemdir);
	Array.sort(RightHemList);
	Array.sort(LeftHemList);

	atlasImages=getFileList(slicedir);
	Array.sort(atlasImages);

	// To determine which image of thresholded consolidated bead image to open in array
	i=0;
	// There is one extra JSON file at the end of the array of atlas images
	stop=atlasImages.length-1;
	for (a = 0; a < stop; a++) {

		//opens the atlas image dimension and applies it to consolidated thresholded bead image
		open(slicedir+atlasImages[a]);
		getDimensions(w, h, channels, slices, frames);
		close();
	
		open(RightHemdir + RightHemList[i]);
		fileName=getTitle();
		run("Scale...", "x=- y=- width=w height=h interpolation=Bilinear average create");
		close(fileName);

		setAutoThreshold("Default");
		run("Threshold...");
		setThreshold(0, 0);
		run("Convert to Mask");
		run("Convert to Mask");
		
		saveAs("png", RightHemdir + fileName);
		close();

		open(LeftHemdir + LeftHemList[i]);
		fileName=getTitle();
		run("Scale...", "x=- y=- width=w height=h interpolation=Bilinear average create");
		close(fileName);

		setAutoThreshold("Default");
		run("Threshold...");
		setThreshold(0, 0);
		run("Convert to Mask");
		run("Convert to Mask");
		
		saveAs("png", LeftHemdir + fileName);
		close();

		// Opens nexts thresholded bead image in the array
		i=i+1;
		// Skips other atlas images from this section
		a=a+3;
}
	
	close("Threshold");

	if (File.exists(dir + "~Nutil OUTPUT")) {
	} else {
		File.makeDirectory(dir + "~Nutil OUTPUT");
		}
	consolidateddir = dir + "~Nutil OUTPUT" + File.separator;

	if (File.exists(consolidateddir + "Left")) {
	} else {
		File.makeDirectory(consolidateddir + "Left");
		}

	if (File.exists(consolidateddir + "Right")) {
	} else {
		File.makeDirectory(consolidateddir + "Right");
		}

}

if (volumecheck == true) {

aligneddir = dir + "2-Aligned Images" + File.separator;
//aligneddir = dir + "2.2-Semi-Automatically Alignment Images" + File.separator;
alignedlist = getFileList(aligneddir);
Array.sort(alignedlist);

imagedir = aligneddir + alignedlist[1]+ File.separator;
imagelist = getFileList(imagedir);
Array.sort(imagelist);

roidir = aligneddir + alignedlist[2]+ File.separator;
roilist = getFileList(roidir);
Array.sort(roilist);

for (i = 0; i < imagelist.length; i++) {
	open(imagedir + imagelist[i]);
	
	//Fall Scale
	//run("Set Scale...", "distance=240.5 known=1 pixel=1 unit=mm");

	//Winter Scale
	run("Set Scale...", "distance=168 known=1 pixel=1 unit=mm");
	
	run("Set Measurements...", "area redirect=None decimal=3");
	image=(getTitle);
	open(roidir + roilist[i]);
	roiManager("select", 0);
	run("Measure");
	
	run("Close All");
	close("ROI Manager");
}

selectWindow("Results");
saveAs("Text", aligneddir + "BrainArea.csv");
close("Results");
	
}


if (beadcheck == true) {


	brainImages=getFileList(autodir);
	Array.sort(brainImages);
	alignedImages=getFileList(autodir + brainImages[0]);
	Array.sort(alignedImages);

	if (File.exists(dir + "4.1-Manual Counts-ROI")) {
	} else {
	File.makeDirectory(dir + "4.1-Manual Counts-ROI");
		}
	manualROIdir = dir + "4.1-Manual Counts-ROI" + File.separator;

	if (File.exists(dir + "4.1-Manual Counts-mask")) {
	} else {
	File.makeDirectory(dir + "4.1-Manual Counts-mask");
		}
	manualmaskdir = dir + "4.1-Manual Counts-mask" + File.separator;

	File.makeDirectory(manualROIdir + brainImages[0]);	
	ROIdir = manualROIdir + brainImages[0] + File.separator;

	//subtract 2 from length of array, since the XML files are also located in this folder
	for (i = 0; i < alignedImages.length-2; i++) {
		open(autodir + brainImages[0] + alignedImages[i]);
		fileName=getTitle();
		run("Maximize");
		setTool("multipoint");
		run("Point Tool...", "type=Dot color=White size=Small counter=0");
		bcc=false;
		Dialog.create("Are microbeads present in the image?");
		Dialog.addCheckbox("Are microbeads present in this image?", bcc);
		Dialog.show();
		bcc = Dialog.getCheckbox();
		if (bcc==true){
			waitForUser("Click all microbeads in image and press Okay");
			roiManager("Add");
			roiManager("Select", 0);
			roiManager("Rename", fileName);
			roiManager("Save", ROIdir + fileName + ".zip");

			fileName=getTitle();
			roiManager("Select", 0);
			run("From ROI Manager");
			run("Flatten");
			close(fileName);
			run("8-bit");
			setThreshold(254, 255);
			setOption("BlackBackground", false);
			run("Convert to Mask");
run("Dilate");
run("Dilate");
run("Dilate");
			saveAs("png", manualmaskdir + fileName);
			
			roiManager("Deselect");
			selectWindow("ROI Manager");
			run("Close");
		}
		else{
			run("Colors...", "foreground=white background=white selection=white");
			run("Select All");
			run("Clear", "slice");
			run("Select None");
			saveAs("png", manualmaskdir + fileName);
		}
	run("Close All");
	}

	images=getFileList(manualmaskdir);
	Array.sort(images);

	if (File.exists(manualmaskdir + "Consolidated Images")) {
	} else {
		File.makeDirectory(manualmaskdir + "Consolidated Images");
		}
	consolidateddir = manualmaskdir + "Consolidated Images" + File.separator;

	stop=images.length-1;

	for (i = 0; i < stop; i++) {
		open(manualmaskdir + images[i]);

		image1=getTitle();
		selectWindow(image1);
		run("Make Binary");

		open(manualmaskdir + images[i+1]);
		image2=getTitle();
		selectWindow(image2);
		run("Make Binary");

		selectWindow(image2);
		run("Dilate");
		run("Dilate");
		run("Dilate");
		run("Dilate");

		imageCalculator("Substract create", image1,image2);
		close(image1);
		close(image2);
		run("Despeckle");
		run("Despeckle");
		run("Despeckle");


//selectWindow("Results");
close("Results");
		
		saveAs("png", consolidateddir + image1);
		close();

	}

// since the last image has nothing to substract from.
	open(manualmaskdir + images[stop]);
	image=getTitle();
	saveAs("png", consolidateddir + image);
	close();
	
}

/////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////
if (visualcheck == true){
	thresholddir = dir+"3-Thresholded Image"+File.separator;
	thresholdlist=getFileList(thresholddir);
	
	alignedBFdir=dir+"2-Aligned Images"+File.separator;
	alignedBF1=getFileList(alignedBFdir);
	//alignedBFdir2=alignedBFdir+alignedBF1[0];
	alignedBFdir2=alignedBFdir+alignedBF1[1];
	alignedBF2=getFileList(alignedBFdir2);

	stop=alignedBF2.length;

		for (i = 0; i < stop; i++) {
			open(alignedBFdir2+alignedBF2[i]);
			imagetitle=getTitle();
			open(thresholddir+thresholdlist[i]);
			thresholdtitle=getTitle();

			run("Merge Channels...", "c1=" + thresholdtitle + " c4=" + imagetitle + " create");
			selectWindow("Composite");
			run("Flatten");
			rename(i);
			selectWindow(i);

			
		}

	run("Images to Stack");
	
}


if (verifycheck == true) {

	manualmaskdir = dir + "4.1-Manual Counts-mask" + File.separator + "Consolidated Images" + File.separator;
	thresholdmaskdir = dir+"3-Thresholded Image"+File.separator + "Consolidated Images" + File.separator;
	
	manualcount=getFileList(manualmaskdir);
	Array.sort(manualcount);
	autocount=getFileList(thresholdmaskdir);
	Array.sort(autocount);

	for (i = 0; i < manualcount.length; i++) {
		open(manualmaskdir + manualcount[i]);

		run("Erode");
		run("Erode");
		
		run("Measure");
		nobeads=getResult("Mean");
		if (nobeads==0){
			count=0;
			selectWindow("Results");
			run("Close");
			close();
		}
		else {
			run("Analyze Particles...", "display summarize");

			selectWindow("Summary"); 
			row = split(getInfo(), "\n");
			headings = split(row[0], "\t");
			objectcount = split(row[1], "\t");

			count=objectcount[1];
			selectWindow("Summary");
			run("Close");
			close();
			selectWindow("Results");
			run("Close");
		}
		print(manualcount[i] + " ," + count);
		}

	selectWindow("Log");
	summaryfile = "Manual Counts" + ".csv";
	saveAs("Text", manualmaskdir+summaryfile);
	selectWindow("Log");
	run("Close");

		for (i = 0; i < autocount.length; i++) {
		open(thresholdmaskdir + autocount[i]);

		run("Measure");
		nobeads=getResult("Mean");
		if (nobeads==0){
			count=0;
			selectWindow("Results");
			run("Close");
			close();
		}
		else {
			run("Analyze Particles...", "display summarize");

			selectWindow("Summary"); 
			row = split(getInfo(), "\n");
			headings = split(row[0], "\t");
			objectcount = split(row[1], "\t");

			count=objectcount[1];
			selectWindow("Summary");
			run("Close");
			close();
			selectWindow("Results");
			run("Close");
		}

		print(autocount[i] + " ," + count);
			
		}

	selectWindow("Log");
	summaryfile = "Auto Counts" + ".csv";
	saveAs("Text", thresholdmaskdir+summaryfile);
	selectWindow("Log");
	run("Close");
}

if(ROIcountcheck==true){


	if (File.exists(dir + "5. Consolidated ROI Counts")) {
	} else {
		File.makeDirectory(dir + "5. Consolidated ROI Counts");
		}
	counteddir = dir + "5. Consolidated ROI Counts" + File.separator;
	
	
	manualmaskcountsdir = dir + "4.1-Manual Counts-mask" + File.separator + "Consolidated Images" + File.separator;
	manualcounts = getFileList(manualmaskcountsdir);
	Array.sort(manualcounts);

	brainImages=getFileList(autodir);
	Array.sort(brainImages);
	alignedImages=getFileList(autodir + brainImages[0]);
	Array.sort(alignedImages);

	beadnum=1;

for (i = 0; i < manualcounts.length-1; i++) {
	open(manualmaskcountsdir + manualcounts[i]);
	imageName=getTitle();
	run("Measure");
	nobeads=getResult("Mean");
		if (nobeads==0){
			count=0;
			selectWindow("Results");
			run("Close");
			close(imageName);
		}
		else {
			selectWindow("Results");
			run("Close");
			run("Analyze Particles...", "add");

			totalbeadsinimage=roiManager("count");
			
				for (b=0;b<totalbeadsinimage;b++){ 
	   			    roiManager("select", b); 
					roiManager("rename", beadnum);
					beadnum=beadnum+1;
					
				} 

			roiManager("Save", counteddir + imageName + ".zip");
			
			run("Close All");
			selectWindow("ROI Manager");
			run("Close");
			}
		}
}

if(dimensioncheck == true){

	waitForUser("Choose directory containing images that you want resized to atlas images from 'QuickNII'");
	maskimagedir=getDirectory("Directory containing images to be resized");
	maskimages = getFileList(maskimagedir);
	Array.sort(maskimages);

	slicedir = dir+"~Export Slices (from Quick NII)"+File.separator;
	atlasImages=getFileList(slicedir);
	Array.sort(atlasImages);

	if (File.exists(dir+"6. Resized Images")) {
	} else {
		File.makeDirectory(dir+"6. Resized Images");
		}
	resizedir = dir+"6. Resized Images"+File.separator;

	// Opens consolidated thresholded bead image array
	i=0;
	// There is 4 extra compiled file at the end of the array of atlas images
	//stop=atlasImages.length-4;
	// There is one extra compiled file at the end of the array of atlas images
	stop=atlasImages.length-1;

	
	for (a = 0; a < stop; a++) {

		//opens the atlas image dimension and applies it to consolidated thresholded bead image
		open(slicedir+atlasImages[a]);
		getDimensions(w, h, channels, slices, frames);
		close();
	
		open(maskimagedir + maskimages[i]);
		fileName=getTitle();
		
		run("Scale...", "x=- y=- width=w height=h interpolation=Bilinear average create");
run("Convert to Mask");
//run("Despeckle");
		
		close(fileName);

run("Measure");
		nobeads=getResult("Mean");
		if (nobeads==255){
			run("RGB Color");

		} else {
			run("Green");
run("RGB Color");
		}

			selectWindow("Results");
			run("Close");


		
		saveAs(resizedir + fileName);
		close();

		// Opens nexts thresholded bead image in the array
		i=i+1;
		// Skips other atlas images from this section
		a=a+3;

	
}


	
}


	
