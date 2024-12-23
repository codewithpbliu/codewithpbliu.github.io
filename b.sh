head title.md |awk -F'>' '{print $3}' |sed 's#</a##g' | while read line
do
  title=`echo $line | awk -F'章' '{print $1}'`
  echo "${title}章"
  echo "* [$line](反派：我的弟弟是天选之子/$line.md)"
done