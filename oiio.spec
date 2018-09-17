#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oiio
Version  : 1.8.14
Release  : 3
URL      : https://github.com/OpenImageIO/oiio/archive/Release-1.8.14.tar.gz
Source0  : https://github.com/OpenImageIO/oiio/archive/Release-1.8.14.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: oiio-bin
Requires: oiio-lib
Requires: oiio-license
Requires: oiio-data
BuildRequires : LibRaw-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : bzip2-dev
BuildRequires : freetype-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libwebp-dev
BuildRequires : mesa-dev
BuildRequires : openexr-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libraw)
BuildRequires : pkgconfig(libraw_r)
BuildRequires : python-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : tiff-dev
BuildRequires : zlib-dev

%description
This test verifies that the texture system is choosing the right mip
levels.  It uses a special texture, miplevels.tx, that uses color codes
for each mip level, and renders a 256x256 image where the texture
coordinates are exactly aligned to the pixel grid.  In miplevels, the
256x256 level is pure green, the 512x512 level is red, the 128x128 is
blue.  So of course we expect the output of this test to be pure green
(except for the text "256" in the center).

%package bin
Summary: bin components for the oiio package.
Group: Binaries
Requires: oiio-data
Requires: oiio-license

%description bin
bin components for the oiio package.


%package data
Summary: data components for the oiio package.
Group: Data

%description data
data components for the oiio package.


%package dev
Summary: dev components for the oiio package.
Group: Development
Requires: oiio-lib
Requires: oiio-bin
Requires: oiio-data
Provides: oiio-devel

%description dev
dev components for the oiio package.


%package doc
Summary: doc components for the oiio package.
Group: Documentation

%description doc
doc components for the oiio package.


%package lib
Summary: lib components for the oiio package.
Group: Libraries
Requires: oiio-data
Requires: oiio-license

%description lib
lib components for the oiio package.


%package license
Summary: license components for the oiio package.
Group: Default

%description license
license components for the oiio package.


%prep
%setup -q -n oiio-Release-1.8.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537216139
unset LD_AS_NEEDED
mkdir clr-build
pushd clr-build
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%cmake .. -DSTOP_ON_WARNING=OFF -DILMBASE_INCLUDE_PATH=/usr/include/OpenEXR -DUSE_PYTHON=OFF
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1537216139
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/oiio
cp LICENSE %{buildroot}/usr/share/doc/oiio/LICENSE
cp src/fonts/Droid_Sans/LICENSE.txt %{buildroot}/usr/share/doc/oiio/src_fonts_Droid_Sans_LICENSE.txt
cp src/fonts/Droid_Sans_Mono/LICENSE.txt %{buildroot}/usr/share/doc/oiio/src_fonts_Droid_Sans_Mono_LICENSE.txt
cp src/fonts/Droid_Serif/LICENSE.txt %{buildroot}/usr/share/doc/oiio/src_fonts_Droid_Serif_LICENSE.txt
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/iconvert
/usr/bin/idiff
/usr/bin/igrep
/usr/bin/iinfo
/usr/bin/maketx
/usr/bin/oiiotool

%files data
%defattr(-,root,root,-)
/usr/share/fonts/OpenImageIO/DroidSans-Bold.ttf
/usr/share/fonts/OpenImageIO/DroidSans.ttf
/usr/share/fonts/OpenImageIO/DroidSansMono.ttf
/usr/share/fonts/OpenImageIO/DroidSerif-Bold.ttf
/usr/share/fonts/OpenImageIO/DroidSerif-BoldItalic.ttf
/usr/share/fonts/OpenImageIO/DroidSerif-Italic.ttf
/usr/share/fonts/OpenImageIO/DroidSerif.ttf

%files dev
%defattr(-,root,root,-)
/usr/include/OpenImageIO/SHA1.h
/usr/include/OpenImageIO/argparse.h
/usr/include/OpenImageIO/array_view.h
/usr/include/OpenImageIO/atomic.h
/usr/include/OpenImageIO/benchmark.h
/usr/include/OpenImageIO/color.h
/usr/include/OpenImageIO/dassert.h
/usr/include/OpenImageIO/deepdata.h
/usr/include/OpenImageIO/errorhandler.h
/usr/include/OpenImageIO/export.h
/usr/include/OpenImageIO/filesystem.h
/usr/include/OpenImageIO/filter.h
/usr/include/OpenImageIO/fmath.h
/usr/include/OpenImageIO/fstream_mingw.h
/usr/include/OpenImageIO/function_view.h
/usr/include/OpenImageIO/hash.h
/usr/include/OpenImageIO/image_view.h
/usr/include/OpenImageIO/imagebuf.h
/usr/include/OpenImageIO/imagebufalgo.h
/usr/include/OpenImageIO/imagebufalgo_util.h
/usr/include/OpenImageIO/imagecache.h
/usr/include/OpenImageIO/imageio.h
/usr/include/OpenImageIO/missing_math.h
/usr/include/OpenImageIO/oiioversion.h
/usr/include/OpenImageIO/optparser.h
/usr/include/OpenImageIO/osdep.h
/usr/include/OpenImageIO/parallel.h
/usr/include/OpenImageIO/paramlist.h
/usr/include/OpenImageIO/platform.h
/usr/include/OpenImageIO/plugin.h
/usr/include/OpenImageIO/pugiconfig.hpp
/usr/include/OpenImageIO/pugixml.cpp
/usr/include/OpenImageIO/pugixml.hpp
/usr/include/OpenImageIO/refcnt.h
/usr/include/OpenImageIO/simd.h
/usr/include/OpenImageIO/span.h
/usr/include/OpenImageIO/strided_ptr.h
/usr/include/OpenImageIO/string_view.h
/usr/include/OpenImageIO/strutil.h
/usr/include/OpenImageIO/sysutil.h
/usr/include/OpenImageIO/texture.h
/usr/include/OpenImageIO/thread.h
/usr/include/OpenImageIO/timer.h
/usr/include/OpenImageIO/tinyformat.h
/usr/include/OpenImageIO/typedesc.h
/usr/include/OpenImageIO/unittest.h
/usr/include/OpenImageIO/unordered_map_concurrent.h
/usr/include/OpenImageIO/ustring.h
/usr/include/OpenImageIO/varyingref.h
/usr/include/OpenImageIO/version.h
/usr/lib64/libOpenImageIO.so
/usr/lib64/libOpenImageIO_Util.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/OpenImageIO/CHANGES.md
/usr/share/doc/OpenImageIO/openimageio.pdf

%files lib
%defattr(-,root,root,-)
/usr/lib64/libOpenImageIO.so.1.8
/usr/lib64/libOpenImageIO.so.1.8.14
/usr/lib64/libOpenImageIO_Util.so.1.8
/usr/lib64/libOpenImageIO_Util.so.1.8.14

%files license
%defattr(-,root,root,-)
/usr/share/doc/OpenImageIO/LICENSE
/usr/share/doc/oiio/LICENSE
/usr/share/doc/oiio/src_fonts_Droid_Sans_LICENSE.txt
/usr/share/doc/oiio/src_fonts_Droid_Sans_Mono_LICENSE.txt
/usr/share/doc/oiio/src_fonts_Droid_Serif_LICENSE.txt
