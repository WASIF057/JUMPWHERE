using Contracts;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.Linq.Expressions;
using System.Net;
using TransmonAdvaita.Data;
using TransmonAdvaita.Model;
using TransmonAdvaita.Services;

namespace TransmonAdvaita.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    [Authorize]
    public class AlchemyDbSetupController : ControllerBase
    {
        private readonly IAlchemyDbSetupService _alchnyDbSetupService;
        private readonly ExternalAdvaitaMasterDbContext _externalAdvaitaDBContext;
        private ILoggerManager _logger;

        public AlchemyDbSetupController(IAlchemyDbSetupService alchnyDbSetupService, ExternalAdvaitaMasterDbContext externalAdvaitaDBContext, ILoggerManager logger)
        {
            _alchnyDbSetupService = alchnyDbSetupService;
            _externalAdvaitaDBContext = externalAdvaitaDBContext;
            _logger = logger;
        }


        [HttpPost]
        public async Task<IActionResult> CreateNewTenantForAlchemy(int orgId)
        {
            ServiceResponse<IEnumerable<dynamic>> serviceResponse = new ServiceResponse<IEnumerable<dynamic>>();
            try
            {
                if (orgId == null || orgId == 0)
                {
                    serviceResponse.Data = null;
                    serviceResponse.Message = "Invalid orgId parameter";
                    serviceResponse.Success = false;
                    serviceResponse.StatusCode = HttpStatusCode.BadRequest;
                    return BadRequest(serviceResponse);
                }
                var newTenantDbName = await _externalAdvaitaDBContext.AdOrganisations
                                      .Where(m => m.Id == orgId)
                                      .Select(x => x.DbName)
                                        .FirstOrDefaultAsync();

                var result = await _alchnyDbSetupService.CreateDbContextWithNewDatabaseNameForNewTenant(newTenantDbName.ToString());
                serviceResponse.Data = null;        //new List<dynamic> { result };
                serviceResponse.Message = "Success";
                serviceResponse.Success = true;
                serviceResponse.StatusCode = HttpStatusCode.OK;
                return Ok(serviceResponse);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex.Message);
                serviceResponse.Data = null;
                serviceResponse.Message = "Inter server error";
                serviceResponse.Success = false;
                serviceResponse.StatusCode = HttpStatusCode.InternalServerError;
                return StatusCode(500, serviceResponse);
            }
        }

    }
}