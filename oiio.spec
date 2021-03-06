#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oiio
Version  : 2.2.15.1
Release  : 33
URL      : https://github.com/OpenImageIO/oiio/archive/Release-2.2.15.1/oiio-2.2.15.1.tar.gz
Source0  : https://github.com/OpenImageIO/oiio/archive/Release-2.2.15.1/oiio-2.2.15.1.tar.gz
Summary  : OpenImageIO is a library for reading and writing images.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: oiio-bin = %{version}-%{release}
Requires: oiio-data = %{version}-%{release}
Requires: oiio-lib = %{version}-%{release}
Requires: oiio-license = %{version}-%{release}
BuildRequires : LibRaw-dev
BuildRequires : OpenColorIO-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : bzip2-dev
BuildRequires : extra-cmake-modules pkgconfig(OpenEXR)
BuildRequires : fmt-dev
BuildRequires : freetype-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libwebp-dev
BuildRequires : mesa-dev
BuildRequires : opencv-dev
BuildRequires : openexr-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(OpenEXR)
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libraw)
BuildRequires : pkgconfig(libraw_r)
BuildRequires : pkgconfig(libswscale)
BuildRequires : pugixml-dev
BuildRequires : python3-dev
BuildRequires : robin-map-dev
BuildRequires : tbb-dev
BuildRequires : tiff-dev
BuildRequires : zlib-dev

%description
LICENSE
-------
The squish library is distributed under the terms and conditions of the MIT
license. This license is specified at the top of each source file and must be
preserved in its entirety.

%package bin
Summary: bin components for the oiio package.
Group: Binaries
Requires: oiio-data = %{version}-%{release}
Requires: oiio-license = %{version}-%{release}

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
Requires: oiio-lib = %{version}-%{release}
Requires: oiio-bin = %{version}-%{release}
Requires: oiio-data = %{version}-%{release}
Provides: oiio-devel = %{version}-%{release}
Requires: oiio = %{version}-%{release}

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
Requires: oiio-data = %{version}-%{release}
Requires: oiio-license = %{version}-%{release}

%description lib
lib components for the oiio package.


%package license
Summary: license components for the oiio package.
Group: Default

%description license
license components for the oiio package.


%prep
%setup -q -n oiio-Release-2.2.15.1
cd %{_builddir}/oiio-Release-2.2.15.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622777281
unset LD_AS_NEEDED
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%cmake .. -Wno-dev \
-DBUILDSTATIC:BOOL=OFF \
-DBUILD_MISSING_FMT:BOOL=OFF \
-DCMAKE_DL_LIBS=dl \
-DCMAKE_INSTALL_DOCDIR:PATH=/usr/share/doc/oiio \
-DCMAKE_INSTALL_MANDIR:PATH=/usr/share/man/man1 \
-DCMAKE_SKIP_RPATH:BOOL=ON \
-DILMBASE_INCLUDE_PATH=/usr/include/OpenEXR \
-DINSTALL_DOCS:BOOL=ON \
-DINSTALL_FONTS:BOOL=ON \
-DLINKSTATIC:BOOL=OFF \
-DOpenGL_GL_PREFERENCE=GLVND \
-DSTOP_ON_WARNING=OFF \
-DUSE_EXTERNAL_PUGIXML:BOOL=ON \
-DUSE_FFMPEG:BOOL=OFF \
-DUSE_OPENCV:BOOL=ON \
-DUSE_OPENSSL:BOOL=ON \
-DUSE_PYTHON:BOOL=OFF
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1622777281
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oiio
cp %{_builddir}/oiio-Release-2.2.15.1/LICENSE.md %{buildroot}/usr/share/package-licenses/oiio/8753cb3fb20c55b0a920e1fbc7d9be770f2be3c6
cp %{_builddir}/oiio-Release-2.2.15.1/src/fonts/Droid_Sans/LICENSE.txt %{buildroot}/usr/share/package-licenses/oiio/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/oiio-Release-2.2.15.1/src/fonts/Droid_Sans_Mono/LICENSE.txt %{buildroot}/usr/share/package-licenses/oiio/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/oiio-Release-2.2.15.1/src/fonts/Droid_Serif/LICENSE.txt %{buildroot}/usr/share/package-licenses/oiio/2b8b815229aa8a61e483fb4ba0588b8b6c491890
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
/usr/bin/iv
/usr/bin/maketx
/usr/bin/oiiotool

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*
/usr/share/fonts/OpenImageIO/DroidSans-Bold.ttf
/usr/share/fonts/OpenImageIO/DroidSans.ttf
/usr/share/fonts/OpenImageIO/DroidSansMono.ttf
/usr/share/fonts/OpenImageIO/DroidSerif-Bold.ttf
/usr/share/fonts/OpenImageIO/DroidSerif-BoldItalic.ttf
/usr/share/fonts/OpenImageIO/DroidSerif-Italic.ttf
/usr/share/fonts/OpenImageIO/DroidSerif.ttf

%files dev
%defattr(-,root,root,-)
/usr/include/OpenImageIO/Imath.h
/usr/include/OpenImageIO/argparse.h
/usr/include/OpenImageIO/array_view.h
/usr/include/OpenImageIO/atomic.h
/usr/include/OpenImageIO/attrdelegate.h
/usr/include/OpenImageIO/benchmark.h
/usr/include/OpenImageIO/color.h
/usr/include/OpenImageIO/dassert.h
/usr/include/OpenImageIO/deepdata.h
/usr/include/OpenImageIO/detail/farmhash.h
/usr/include/OpenImageIO/detail/fmt/core.h
/usr/include/OpenImageIO/detail/fmt/format-inl.h
/usr/include/OpenImageIO/detail/fmt/format.h
/usr/include/OpenImageIO/detail/fmt/ostream.h
/usr/include/OpenImageIO/detail/fmt/printf.h
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
/usr/include/OpenImageIO/parallel.h
/usr/include/OpenImageIO/paramlist.h
/usr/include/OpenImageIO/platform.h
/usr/include/OpenImageIO/plugin.h
/usr/include/OpenImageIO/refcnt.h
/usr/include/OpenImageIO/simd.h
/usr/include/OpenImageIO/span.h
/usr/include/OpenImageIO/strided_ptr.h
/usr/include/OpenImageIO/string_view.h
/usr/include/OpenImageIO/strutil.h
/usr/include/OpenImageIO/sysutil.h
/usr/include/OpenImageIO/texture.h
/usr/include/OpenImageIO/thread.h
/usr/include/OpenImageIO/tiffutils.h
/usr/include/OpenImageIO/timer.h
/usr/include/OpenImageIO/typedesc.h
/usr/include/OpenImageIO/unittest.h
/usr/include/OpenImageIO/unordered_map_concurrent.h
/usr/include/OpenImageIO/ustring.h
/usr/include/OpenImageIO/varyingref.h
/usr/include/OpenImageIO/version.h
/usr/lib64/cmake/OpenImageIO/OpenImageIOConfig.cmake
/usr/lib64/cmake/OpenImageIO/OpenImageIOConfigVersion.cmake
/usr/lib64/cmake/OpenImageIO/OpenImageIOTargets-relwithdebinfo.cmake
/usr/lib64/cmake/OpenImageIO/OpenImageIOTargets.cmake
/usr/lib64/libOpenImageIO.so
/usr/lib64/libOpenImageIO_Util.so
/usr/lib64/pkgconfig/OpenImageIO.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/oiio/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libOpenImageIO.so.2.2
/usr/lib64/libOpenImageIO.so.2.2.15
/usr/lib64/libOpenImageIO_Util.so.2.2
/usr/lib64/libOpenImageIO_Util.so.2.2.15

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oiio/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/oiio/8753cb3fb20c55b0a920e1fbc7d9be770f2be3c6
