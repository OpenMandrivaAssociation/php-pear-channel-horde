%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)
%define pear_xmldir  %{_datadir}/pear/packages

Name:           php-pear-channel-horde
Version:        1.0
Release:        12
Summary:        Adds pear.horde.org channel to PEAR
Group:          System/Libraries
License:        BSD
URL:            http://pear.horde.org/
Source0:        http://pear.horde.org/channel.xml
BuildArch:      noarch
BuildRequires:  php-pear >= 5.1.1
Requires(pre):	php-cli
Requires(pre):	php-pear
Requires:	php-mbstring
Requires:	php-mysql
Requires:	php-session
Requires:	php-sysvsem
Requires:	php-tokenizer




%description
This package adds the pear.horde.org channel which allows PEAR packages
from this channel to be installed.


%prep
%setup -q -c -T


%build
# Empty build section, nothing to build


%install

%{__mkdir_p} %{buildroot}%{pear_xmldir}
%{__install} -pm 644 %{SOURCE0} %{buildroot}%{pear_xmldir}/pear.horde.org.xml



%post
if [ $1 -gt  1 ] ; then
   pear channel-update pear.horde.org
else
   pear channel-add %{pear_xmldir}/pear.horde.org.xml
fi

%preun
if [ $1 -eq 0 ] ; then
   pear channel-delete pear.horde.org
fi


%files
%defattr(-,root,root,-)
%{pear_xmldir}/pear.horde.org.xml


%changelog
* Tue Mar 27 2012 Thomas Spuhler <tspuhler@mandriva.org> 1.0-10mdv2012.0
+ Revision: 787366
- changed channel-upgrade from local to net so it will actually upgrade

* Wed Mar 14 2012 Thomas Spuhler <tspuhler@mandriva.org> 1.0-9
+ Revision: 784910
- post and postun revised so it will update the channel

* Sun Dec 18 2011 Thomas Spuhler <tspuhler@mandriva.org> 1.0-8
+ Revision: 743619
- updated the channel address
- corrected the channel addresses

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-7
+ Revision: 679622
- mass rebuild

* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 1.0-6mdv2011.0
+ Revision: 564123
- Increased release for rebuild

* Thu May 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-5mdv2010.1
+ Revision: 543021
- try to fix a problem reported by Thomas Spuhler

* Sun Feb 21 2010 Thomas Spuhler <tspuhler@mandriva.org> 1.0-4mdv2010.1
+ Revision: 509253
- updated rel to 4
-added nl at the end of channel.xml

* Sun Feb 14 2010 Thomas Spuhler <tspuhler@mandriva.org> 1.0-3mdv2010.1
+ Revision: 505666
- increase version to move to main

* Sat Feb 13 2010 Thomas Spuhler <tspuhler@mandriva.org> 1.0-2mdv2010.1
+ Revision: 505541
-- dealed PreRequ line. It's php-pear is always installed on our system
- PreReq was  php  php-pear >= 5.1.1
- added buildroot line
- corrected Group name
- intital build for kolab-filter
- import php-pear-channel-horde


