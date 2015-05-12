<?php
class SimpleStegano{
	private $imagePath;
	private $message;
	public $msg_ori;
	public function __construct($imgPath,$msg)
	{
		$this->msg_ori = $msg;
		$this->message = $this->MsgToBiner($msg);
		$this->imagePath = $imgPath;
	}
	
	function show_msg() {
		return $this->message;
	}
	
	function oriPixel()
	{
		$i = 0;
		$lenmsg = strlen($this->message);
		$image = imagecreatefrompng($this->imagePath);
		$width = imagesx($image);
		$height = imagesy($image);
		$res = '';
		for ($y = 0; $y <$height; $y++)
		{
			for ($x = 0; $x <$width; $x++){
				if($i == $lenmsg) break;
				$rgb = imagecolorat($image, $x, $y);
				$r = ($rgb >> 16) & 0xFF;
				$g = ($rgb >> 8) & 0xFF;
				$b = $rgb & 0xFF;
				
				if($i<$lenmsg)
				{
					$res .= $r.' - ';
					$i++;
				}
				if($i<$lenmsg)
				{
					$res .= $g.' - ';
					$i++;
				}
				if($i<$lenmsg)
				{
					$res .= $b.' - ';
					$i++;
				}
			}
		}
		return $res;
	}
	
	public function LSB()
	{
		$i = 0;
		$lenmsg = strlen($this->message);
		$image = imagecreatefrompng($this->imagePath);
		$image2 = imagecreatefrompng($this->imagePath);
		$width = imagesx($image);
		$height = imagesy($image);
		$image_p = imagecreatetruecolor($width, $height);
		for ($y = 0; $y <$height ; $y++)
		{
			for ($x = 0; $x <$width; $x++){
				if($i == $lenmsg) break;
				$rgb = imagecolorat($image2, $x, $y);
				$r = ($rgb >> 16) & 0xFF;
				$g = ($rgb >> 8) & 0xFF;
				$b = $rgb & 0xFF;
				
				if($i<$lenmsg)
				{
					if($r%2==0 && $this->message[$i]==="1"){$r++;}
					else if($r%2==1 && $this->message[$i]==="0"){$r--;}
					$i++;
				}
				if($i<$lenmsg)
				{
					if($g%2==0 && $this->message[$i]==="1"){$g++;}
					else if($g%2==1 && $this->message[$i]==="0"){$g--;}
					$i++;
				}
				if($i<$lenmsg)
				{
					if($b%2==0 && $this->message[$i]==="1"){$b++;}
					else if($b%2==1 && $this->message[$i]==="0"){$b--;}
					$i++;
				}
				$color =  imagecolorallocate($image,$r,$g,$b);
				imagesetpixel($image,$x,$y,$color);
			}
		}
		imagedestroy($image2);
		imagecopyresampled($image_p, $image, 0, 0, 0, 0, $width, $height, $width, $height);
		return $image_p;
	}
	public function GetMsgFromImage($imageStegano)
	{
		$i = 0;
		$lenmsg = strlen($this->message);
		$image = imagecreatefrompng($imageStegano);
		$width = imagesx($image);
		$height = imagesy($image);
		
		$msg = "";
		for ($x = 0; $x <$height; $x++)
		{
			for ($y = 0; $y <$width ; $y++){
				if($i == $lenmsg) break;
				$rgb = imagecolorat($image, $y, $x);
				$r = ($rgb >> 16) & 0xFF;
				$g = ($rgb >> 8) & 0xFF;
				$b = $rgb & 0xFF;
				if($i<$lenmsg)
				{
					$r = $this->dectobin8bit($r);
					$msg .= substr($r,7,7);
					$i++;
				}
				if($i<$lenmsg)
				{
					$g = $this->dectobin8bit($g);
					$msg .= substr($g,7,7);
					$i++;
				}
				if($i<$lenmsg)
				{
					$b = $this->dectobin8bit($b);
					$msg .= substr($b,7,7);
					$i++;
				}
				
			}
		}
		return $msg;
	}
	public function dectobin8bit($val)
	{
		$biner = decbin($val);
		$len = strlen($biner);
		switch($len)
		{
			case 1 : $biner = "0000000".$biner; break;
			case 2 : $biner = "000000".$biner; break;
			case 3 : $biner = "00000".$biner; break;
			case 4 : $biner = "0000".$biner; break;
			case 5 : $biner = "000".$biner; break;
			case 6 : $biner = "00".$biner; break;
			case 7 : $biner = "0".$biner; break;
			default : continue;
		}
		return $biner;
	}
	public function MsgToBiner($text)
	{
		$result = "";
		$len = strlen($text);
		for($i=0;$i<$len;$i++)
		{
		//echo ord($text[$i]);
			$result.= $this->dectobin8bit(ord($text[$i]));
		}
		return $result;
	}
	public function BinerToMsg($bin)
	{
		$result = "";
		$len = strlen($bin);
		while($len>=0)
		{
			$charbinner = substr($bin,0,8);
			$len = strlen($bin);
			$result.=chr(bindec($charbinner));
			if($len<=8){break;}
			$bin = substr($bin,8,$len);
		}
		return $result;
	}
}
$file = 'image/Ontology.png';
$pesan = 'ayo belajar steganography. simple steganography by bima heweh :v';
$stgno = new SimpleStegano($file,$pesan);
echo $stgno->msg_ori."<br/>";
?>
<html>
<head></head>
<body>
<form action="" method="post">
	<input type="radio" name="a" value="1"/>hidden msg
	<input type="radio" name="a" value="2"/>read msg from image
	<input type="radio" name="a" value="3"/>original img
	<input type="submit" name="" value="check"/>
</form>
</body>
</html>
<?php
if(isset($_POST['a'])){
if($_POST['a']==1){

$wkwk = $stgno->LSB('imageStegano.png');
// header('Content-Type: image/png'); // kalo mau langsung didownload yang ini
// header("Content-Disposition: attachment; filename=imageStegano.png");
// imagepng($wkwk,null,0);

if(imagepng($wkwk,'imageStegano.png',0))
{
	echo "sukses menyisipkan pesan pada gambar imageStegano.png";
}
imagedestroy($wkwk);
}
if($_POST['a']==2){
$msg = $stgno->GetMsgFromImage('imageStegano.png');
echo $stgno->BinerToMsg($msg);
}
if($_POST['a']==3){
$msg = $stgno->oriPixel();
echo $msg;
}
}