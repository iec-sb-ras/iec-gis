from logging.config import dictConfig
import logging
from config import LogConfig

from typing import Dict, Any

from fastapi import FastAPI, Request, Response

dictConfig(LogConfig().dict())
logger = logging.getLogger("wfs")

# logger.info("Dummy Info")
# logger.error("Dummy Error")
logger.debug("Started server")
# logger.warning("Dummy Warning")


app = FastAPI()


A = '''<WFS_Capabilities version="2.0.0" xmlns="http://www.opengis.net/wfs/2.0" xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:ogc="http://www.opengis.net/ogc" xmlns:fes="http://www.opengis.net/fes/2.0" xmlns:gml="http://www.opengis.net/gml" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/wfs/2.0 http://schemas.opengis.net/wfs/2.0/wfs.xsd">
  <ows:ServiceIdentification>
    <ows:Title>WFS 2.0.0 CITE Setup</ows:Title>
    <ows:Abstract></ows:Abstract>
    <ows:ServiceType codeSpace="http://www.opengeospatial.org/">WFS</ows:ServiceType>
    <ows:ServiceTypeVersion>2.0.0</ows:ServiceTypeVersion>
  </ows:ServiceIdentification>
  <ows:OperationsMetadata>
    <ows:Operation name="GetCapabilities">
      <ows:DCP>
        <ows:HTTP>
          <ows:Get xlink:href="https://cite.deegree.org/deegree-webservices-3.5.0/services/wfs200?"/>
          <ows:Post xlink:href="https://cite.deegree.org/deegree-webservices-3.5.0/services/wfs200"/>
        </ows:HTTP>
      </ows:DCP>
      <ows:Parameter name="AcceptVersions">
        <ows:AllowedValues>
          <ows:Value>2.0.0</ows:Value>
        </ows:AllowedValues>
      </ows:Parameter>
    </ows:Operation>
    <ows:Operation name="GetFeature">
      <ows:DCP>
        <ows:HTTP>
          <ows:Get xlink:href="https://cite.deegree.org/deegree-webservices-3.5.0/services/wfs200?"/>
          <ows:Post xlink:href="https://cite.deegree.org/deegree-webservices-3.5.0/services/wfs200"/>
        </ows:HTTP>
      </ows:DCP>
    </ows:Operation>
</ows:OperationsMetadata>
  <FeatureTypeList>
    <FeatureType>
      <Name xmlns:gn="urn:x-inspire:specification:gmlas:GeographicalNames:3.0">gn:NamedPlace</Name>
      <Title>gn:NamedPlace</Title>
      <DefaultCRS>urn:ogc:def:crs:EPSG::4326</DefaultCRS>
      <OutputFormats>
        <Format>application/xml; subtype="gml/3.2.1"</Format>
      </OutputFormats>
      <ows:WGS84BoundingBox>
        <ows:LowerCorner>-180.000000 -90.000000</ows:LowerCorner>
        <ows:UpperCorner>180.000000 90.000000</ows:UpperCorner>
      </ows:WGS84BoundingBox>
    </FeatureType>
    <FeatureType>
      <Name xmlns:ps="urn:x-inspire:specification:gmlas:ProtectedSites:3.0">ps:ProtectedSite</Name>
      <Title>ps:ProtectedSite</Title>
      <DefaultCRS>urn:ogc:def:crs:EPSG::4326</DefaultCRS>
      <OutputFormats>
        <Format>application/xml; subtype="gml/3.2.1"</Format>
      </OutputFormats>
      <ows:WGS84BoundingBox>
        <ows:LowerCorner>4.486395 51.604992</ows:LowerCorner>
        <ows:UpperCorner>5.928631 51.680515</ows:UpperCorner>
      </ows:WGS84BoundingBox>
    </FeatureType>
  </FeatureTypeList>
  <fes:Spatial_Capabilities>
    <fes:GeometryOperands xmlns:gml="http://www.opengis.net/gml" xmlns:gml32="http://www.opengis.net/gml">
      <fes:GeometryOperand name="gml:Box"/>
      <fes:GeometryOperand name="gml:Envelope"/>
      <fes:GeometryOperand name="gml:Point"/>
      <fes:GeometryOperand name="gml:LineString"/>
      <fes:GeometryOperand name="gml:Curve"/>
      <fes:GeometryOperand name="gml:Polygon"/>
    </fes:GeometryOperands>
    <fes:SpatialOperators>
      <fes:SpatialOperator name="BBOX"/>
      <fes:SpatialOperator name="Intersects"/>
      <fes:SpatialOperator name="Contains"/>
      <fes:SpatialOperator name="Beyond"/>
    </fes:SpatialOperators>
  </fes:Spatial_Capabilities>
</WFS_Capabilities>'''

@app.get("/wfs200/wfs_gateway")
#async def root(reqest: Request):
async def root(SERVICE: str = 'VFS',
               REQUEST: str = None,
               ACCEPTVERSIONS: list = []):
    # SERVICE=WFS&REQUEST=GetCapabilities&ACCEPTVERSIONS=2.0.0,1.1.0,1.0.0
    # logger.debug("HERE")
    logger.debug("ACCEP:{}".format(ACCEPTVERSIONS))
    logger.info("GET")
    # logger.error("Dummy Error")
    # logger.debug("Started server")
    # logger.warning("Dummy Warning")
    # sad
    return Response(content=A, media_type="application/xml")

@app.post("/wfs200/")
async def root():
    # SERVICE=WFS&REQUEST=GetCapabilities&ACCEPTVERSIONS=2.0.0,1.1.0,1.0.0
    # logger.debug("HERE")
    logger.debug("ACCEP:{}".format(SERVICE))
    logger.info("POST")
    # logger.error("Dummy Error")
    # logger.debug("Started server")
    # logger.warning("Dummy Warning")
    # sad
    return {"message": "Hello World"}
