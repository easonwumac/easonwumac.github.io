import sys
import os.path
import xml.etree.ElementTree

bundle_name = sys.argv[1]
version = sys.argv[2]
message = sys.argv[3]

print bundle_name + ' ' + version + ' ' + message

dirpath = os.path.join('depictions', bundle_name) 

print 'edit package ' + dirpath ;

et = xml.etree.ElementTree.parse(os.path.join(dirpath, 'info.xml'))

version_tag = et.getroot().find('version')

print version_tag.text
print 'current version ' + version_tag.text + ' to ' + version

version_tag.text = version


changelog_tag = et.getroot().find('changelog')
change_tag = changelog_tag.find('change')

change_tag.text = message

et.write(os.path.join(dirpath, 'info.xml'))


#et = xml.etree.ElementTree.parse(os.path.join(dirpath, 'changelog.xml'))

#new_changes_tag = xml.etree.ElementTree.SubElement(et.getroot(), 'changes')
#version_tag = xml.etree.ElementTree.SubElement(new_changes_tag, 'version')
#change_tag = xml.etree.ElementTree.SubElement(new_changes_tag, 'change')

#version_tag.text = version
#change_tag.text = message

#et.write(os.path.join(dirpath, 'changelog.xml'))